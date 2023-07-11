from urllib.parse import quote

from flask import jsonify, request, make_response

from app import app
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


@app.route('/parse')
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
