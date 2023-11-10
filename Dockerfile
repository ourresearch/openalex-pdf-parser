FROM python:3.11
LABEL authors="nolan"
EXPOSE 5000

RUN mkdir /home/openalex-pdf-parser
WORKDIR /home/openalex-pdf-parser

RUN apt-get update
RUN apt-get -y install wkhtmltopdf

ADD ./ /home/openalex-pdf-parser/
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "33"]