import io
import os
from urllib.parse import quote

from fastapi import Request, Response, BackgroundTasks, FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse

from exceptions import APIError
from pdf.controller import PDFController

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


@app.get('/parse')
async def parse_pdf(doi):
    pdf_c = PDFController(doi)
    await pdf_c.init()
    msg = await pdf_c.parser.parse()
    if doi.startswith('http'):
        doi = doi.split('doi.org/')[1]
    return {
        "message": msg,
        "metadata": {
            "parser": pdf_c.parser.parser_name,
            "doi": doi,
            "doi_url": f"https://doi.org/{doi}",
        },
    }


@app.get('/view')
async def view_pdf(doi, background_tasks: BackgroundTasks):
    pdf_c = PDFController(doi, force_pdf=True)
    await pdf_c.init()
    buffer = io.BytesIO(pdf_c.pdf)
    background_tasks.add_task(buffer.close)
    headers = {
        'Content-Disposition': 'inline; filename=%s.pdf' % f'{quote(doi, safe="")}.pdf'}
    return Response(buffer.getvalue(), headers=headers,
                    media_type='application/pdf')


# if __name__ == "__main__":
#     uvicorn.run('app:app', host="0.0.0.0", port=5000)
