import gzip
from threading import Lock

import os
from urllib.parse import quote

import aioboto3
import botocore

from exceptions import S3FileNotFoundError
from pdf.grobid import GrobidParser
from pdf.utils.string_utils import normalize_doi

S3_LOCK = Lock()
S3_PDF_BUCKET_NAME = os.getenv('AWS_S3_PDF_BUCKET')
S3_GROBID_XML_BUCKET_NAME = os.getenv('AWS_S3_GROBID_XML_BUCKET')
session = aioboto3.Session()


def doi_to_xml_key(doi):
    return f'{quote(doi, safe="")}.xml'


class PDFController:

    def __init__(self, doi, force_pdf=False):
        self.doi = normalize_doi(doi)
        self.force_pdf = force_pdf
        self.cached_resp = None
        self.parser = None
        self.pdf = None
        self.boto_session = aioboto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

    async def init(self):
        async with self.boto_session.client('s3') as s3:
            if self.force_pdf:
                self.pdf = await self.get_pdf_contents(s3)
                return
            self.cached_resp = await self.try_get_cached_grobid(s3)
            self.pdf = None
            if self.cached_resp:
                self.parser = GrobidParser(cached_resp=self.cached_resp)
            else:
                self.pdf = await self.get_pdf_contents(s3)
                self.parser = GrobidParser(pdf_contents=self.pdf)

    async def try_get_cached_grobid(self, s3):
        xml_key = doi_to_xml_key(self.doi)
        try:
            grobid_xml_obj = await s3.get_object(
                Bucket=S3_GROBID_XML_BUCKET_NAME,
                Key=xml_key)
            body = await grobid_xml_obj['Body'].read()
            if body[:3] == b'\x1f\x8b\x08':
                body = gzip.decompress(body)
            print(f'Cache hit for DOI: {self.doi}')
            return body
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] in {"404", "NoSuchKey"}:
                return None

    async def get_pdf_contents(self, s3):
        key = f'{quote(self.doi, safe="")}.pdf'
        try:
            obj_details = await s3.get_object(Bucket=S3_PDF_BUCKET_NAME, Key=key)
            body = await obj_details['Body'].read()
            if body[:3] == b'\x1f\x8b\x08':
                body = gzip.decompress(body)
            return body
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] in {"404", "NoSuchKey"}:
                raise S3FileNotFoundError()
            else:
                raise e
