from functools import wraps
from urllib.parse import quote

from flask import jsonify, request, make_response

from app import app, PDF_PARSER_API_KEY
from exceptions import APIError
from pdf.controller import PDFController


@app.route("/")
def home():
    return jsonify(
        {
            "version": "0.1",
            "app_name": "openalex-pdf-parser",
            "msg": "Don't panic",
        }
    )

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key') or request.args.get('api_key')
        if not api_key or api_key != PDF_PARSER_API_KEY:
            return jsonify({"message": "Invalid or missing API Key"}), 403
        return view_function(*args, **kwargs)
    return decorated_function

@app.route('/parse')
@require_api_key
def parse_pdf():
    doi = request.args.get("doi")
    pdf_c = PDFController(doi)
    msg = pdf_c.parser.parse()
    if doi.startswith('http'):
        doi = doi.split('doi.org/')[1]
    response = {
        "message": msg,
        "metadata": {
            "parser": pdf_c.parser.parser_name,
            "doi": doi,
            "doi_url": f"https://doi.org/{doi}",
        },
    }
    return jsonify(response)

@app.route('/view')
@require_api_key
def view_pdf():
    doi = request.args.get("doi")
    pdf_c = PDFController(doi)
    response = make_response(pdf_c.pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'inline; filename=%s.pdf' % f'{quote(doi, safe="")}.pdf'
    return response



@app.errorhandler(APIError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {"error": err.description, "message": ""}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    # Add some logging so that we can monitor different types of errors
    app.logger.error("{}: {}".format(err.description, response["message"]))
    return jsonify(response), err.code


if __name__ == "__main__":
    app.run()
