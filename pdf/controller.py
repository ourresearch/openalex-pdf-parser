import gzip
from threading import Lock

import os
from urllib.parse import quote

import boto3
import botocore

from exceptions import S3FileNotFoundError
from pdf.grobid import GrobidParser
from pdf.utils.string_utils import normalize_doi

S3_LOCK = Lock()
S3_PDF_BUCKET_NAME = os.getenv('AWS_S3_PDF_BUCKET')
session = boto3.session.Session()

S3 = session.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))


class PDFController:

    def __init__(self, doi):
        self.doi = normalize_doi(doi)
        self.pdf = self.get_pdf_contents()
        self.parser = GrobidParser(self.pdf)

    def get_pdf_contents(self):
        key = f'{quote(self.doi, safe="")}.pdf'
        with S3_LOCK:
            try:
                obj_details = S3.get_object(Bucket=S3_PDF_BUCKET_NAME, Key=key)
                body = obj_details['Body'].read()
                if body[:3] == b'\x1f\x8b\x08':
                    body = gzip.decompress(body)
                return body
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] in {"404", "NoSuchKey"}:
                    raise S3FileNotFoundError()
                else:
                    raise e

