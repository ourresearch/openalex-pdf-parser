FROM python:3.11-bullseye
LABEL authors="nolan"
EXPOSE 5000

RUN apt-get update \
    && apt-get install -y \
        curl \
        libxrender1 \
        libjpeg62-turbo \
        fontconfig \
        libxtst6 \
        xfonts-75dpi \
        xfonts-base \
        xz-utils
RUN curl "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bullseye_amd64.deb" -L -o "wkhtmltopdf.deb"
RUN dpkg -i wkhtmltopdf.deb


RUN mkdir /home/openalex-pdf-parser
WORKDIR /home/openalex-pdf-parser

ADD ./ /home/openalex-pdf-parser/
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "33"]