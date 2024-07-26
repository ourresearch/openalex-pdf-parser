import gzip
from threading import Lock

import os
from urllib.parse import quote

import aioboto3
import botocore

from exceptions import S3FileNotFoundError
from log import logger
from parse.grobid import GrobidParser
from parse.utils.const import PDF_ARCHIVE_BUCKET, GROBID_XML_BUCKET, \
    HTML_ARCHIVE_BUCKET
from parse.utils.pdf_util import PDFVersion, landing_page_key
from parse.utils.string_utils import normalize_doi

S3_LOCK = Lock()
session = aioboto3.Session()


class PDFController:

    def __init__(self, doi, version: PDFVersion, force_pdf=False,
                 bypass_cache=False):
        self.doi = normalize_doi(doi)
        self.version = version
        self.force_pdf = force_pdf
        self.cached_resp = None
        self.bypass_cache = bypass_cache
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
            self.cached_resp = await self.try_get_cached_grobid(s3) if not self.bypass_cache else None
            self.pdf = None
            if self.cached_resp:
                self.parser = GrobidParser(cached_resp=self.cached_resp)
            else:
                self.pdf = await self.get_pdf_contents(s3)
                self.parser = GrobidParser(pdf_contents=self.pdf)

    async def try_get_cached_grobid(self, s3):
        xml_key = self.version.grobid_s3_key(self.doi)
        try:
            grobid_xml_obj = await s3.get_object(
                Bucket=GROBID_XML_BUCKET,
                Key=xml_key)
            body = await grobid_xml_obj['Body'].read()
            if body[:3] == b'\x1f\x8b\x08':
                body = gzip.decompress(body)
            logger.info(f'Cache hit for DOI: {self.doi}')
            return body
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] in {"404", "NoSuchKey"}:
                return None

    async def try_get_pdf_contents(self, s3, bucket=PDF_ARCHIVE_BUCKET):
        if bucket == PDF_ARCHIVE_BUCKET:
            key = self.version.s3_key(self.doi)
        elif bucket == HTML_ARCHIVE_BUCKET:
            key = landing_page_key(self.doi)
        else:
            raise ValueError(f'Invalid S3 Bucket: {bucket}')
        try:
            obj_details = await s3.get_object(Bucket=bucket, Key=key)
            body = await obj_details['Body'].read()
            if body[:3] == b'\x1f\x8b\x08':
                body = gzip.decompress(body)
            return body
        except botocore.exceptions.ClientError as e:
            return None

    async def get_pdf_contents(self, s3):
        for bucket in [PDF_ARCHIVE_BUCKET, HTML_ARCHIVE_BUCKET]:
            pdf_contents = await self.try_get_pdf_contents(s3, bucket)
            if pdf_contents is not None:
                return pdf_contents
        raise S3FileNotFoundError()
