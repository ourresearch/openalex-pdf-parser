import io
import logging
import os
from urllib.parse import quote

import uvicorn
from fastapi import Request, Response, BackgroundTasks, FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from starlette.responses import StreamingResponse

from exceptions import APIError
from parse.pdf_controller import PDFController

from parse.html_controller import HTMLController
from parse.utils.pdf_util import PDFVersion

app = FastAPI()

PDF_PARSER_API_KEY = os.getenv("PDF_PARSER_API_KEY")


@app.get("/")
async def home():
    return {
        "version": "0.1",
        "app_name": "openalex-pdf-parser",
        "msg": "Don't panic",
    }


@app.exception_handler(APIError)
async def unicorn_exception_handler(request: Request, exc: APIError):
    return JSONResponse(
        status_code=exc.code,
        content={
            "message": exc.description},
    )


@app.middleware('http')
async def require_api_key(request: Request, call_next):
    api_key = request.query_params.get('api_key')
    if not api_key or api_key != PDF_PARSER_API_KEY:
        return PlainTextResponse('Invalid or missing API key', status_code=403)
    return await call_next(request)


@app.get('/parse-html')
async def parse_html(doi, include_raw: bool | None = False,
                     try_stylize: bool | None = False):
    if doi.startswith('http'):
        doi = doi.split('doi.org/')[-1]
    html_c = HTMLController(doi, try_stylize=try_stylize)
    await html_c.init()
    msg = await html_c.parser.parse()
    if not include_raw:
        del msg['raw']
    return {
        "message": msg,
        "metadata": {
            "parser": html_c.parser.parser_name,
            "view_url": "https://parseland.herokuapp.com/view?doi=" + doi,
            "html_parse_url": "https://parseland.herokuapp.com/parse-publisher?doi=" + doi,
            "doi": doi,
            "doi_url": f"https://doi.org/{doi}",
        },
    }


@app.get('/parse')
async def parse_pdf(doi, version: str | None = None,
                    include_raw: bool | None = True):
    if not version:
        version = 'published'
    pdf_c = PDFController(doi, PDFVersion.from_version_str(version))
    await pdf_c.init()
    msg = await pdf_c.parser.parse()
    if doi.startswith('http'):
        doi = doi.split('doi.org/')[1]
    if not include_raw:
        del msg['raw']
    return {
        "message": msg,
        "metadata": {
            "parser": pdf_c.parser.parser_name,
            "doi": doi,
            "doi_url": f"https://doi.org/{doi}",
        },
    }


@app.get('/view')
async def view_pdf(doi, background_tasks: BackgroundTasks,
                   version: str | None = 'published'):
    pdf_c = PDFController(doi, PDFVersion.from_version_str(version),
                          force_pdf=True)
    await pdf_c.init()
    buffer = io.BytesIO(pdf_c.pdf)
    background_tasks.add_task(buffer.close)
    headers = {
        'Content-Disposition': 'inline; filename=%s.pdf' % f'{quote(doi, safe="")}.pdf'}
    return Response(buffer.getvalue(), headers=headers,
                    media_type='application/pdf')


@app.get('/download')
async def download_pdf(doi, background_tasks: BackgroundTasks,
                   version: str | None = 'published'):
    pdf_c = PDFController(doi, PDFVersion.from_version_str(version),
                          force_pdf=True)
    await pdf_c.init()
    buffer = io.BytesIO(pdf_c.pdf)
    background_tasks.add_task(buffer.close)
    response = StreamingResponse(buffer, media_type="application/pdf")
    response.headers["Content-Disposition"] = f"attachment; filename={doi}.pdf"
    return response


if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=int(os.getenv('PORT')),
                workers=4)
