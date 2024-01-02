import base64
import gzip
import os
import re
from collections import Counter
from io import BytesIO
from threading import Lock
from urllib.parse import quote, urlparse

import aioboto3
import botocore
import httpx
import pdfkit
from PIL import Image
from bs4 import BeautifulSoup
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from exceptions import S3FileNotFoundError
from parse.grobid import GrobidParser

S3_LOCK = Lock()
S3_HTML_BUCKET_NAME = os.getenv('AWS_S3_HTML_BUCKET')

session = aioboto3.Session()


def doi_to_html_key(doi):
    return f'{quote(doi, safe="")}'


class HTMLController:

    def __init__(self, doi, try_stylize=False):
        self.doi = doi
        self.parser = None
        self.try_stylize = try_stylize
        self.boto_session = aioboto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

    @classmethod
    def most_frequent_domain(cls, html_string):
        url_pattern = re.compile(r'https?://([a-zA-Z0-9.-]+)')
        matches = re.findall(url_pattern, html_string)
        domain_counter = Counter(matches)
        mfd = domain_counter.most_common(1)
        return mfd[0][0] if mfd else None

    @classmethod
    def try_get_base_url(cls, soup):
        if canonical := soup.find("link", {"rel": "canonical"}):
            return urlparse(canonical.get('href')).netloc
        elif base := soup.find('base'):
            return urlparse(base.get('href')).netloc
        elif meta := soup.select_one('meta[name*=url]'):
            return urlparse(meta.get('content')).netloc
        return cls.most_frequent_domain(str(soup))

    @classmethod
    def clean_html(cls, soup, try_stylize=False):
        if try_stylize and (domain := cls.try_get_base_url(soup)):
            tag = soup.new_tag(name='base', attrs={'href': 'https://' + domain})
            soup.select_one('html').insert(0, tag)
            stylized = True
        else:
            for tag in soup.select('[src]'):
                tag.decompose()
            for tag in soup.select('[href]'):
                tag['href'] = ''
            stylized = False
        return soup, stylized

    async def get_s3_pdf(self):
        async with self.boto_session.client('s3') as s3:
            html = await self.get_html(s3)
            soup = BeautifulSoup(html, parser='lxml', features='lxml')
            cleaned, stylized = self.clean_html(soup,
                                                try_stylize=self.try_stylize)
            opts = {"load-error-handling": "ignore",
                    'load-media-error-handling': 'ignore',
                    'disable-javascript': '',
                    'log-level': 'info',
            }
            if not stylized:
                opts.update({
                    'no-images': "",
                    'disable-external-links': '',
                    'disable-internal-links': '',
                })
            pdf = pdfkit.from_string(str(cleaned),
                                     options=opts,
                                     verbose=True)
        return pdf

    async def init(self):
        pdf = await self.get_s3_pdf()
        self.parser = GrobidParser(pdf_contents=pdf)

    async def get_html(self, s3):
        key = doi_to_html_key(self.doi)
        try:
            obj = await s3.get_object(
                Bucket=S3_HTML_BUCKET_NAME,
                Key=key)
            body = await obj['Body'].read()
            if body[:3] == b'\x1f\x8b\x08':
                body = gzip.decompress(body)
            return body
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] in {"404", "NoSuchKey"}:
                raise S3FileNotFoundError(e)

    async def get_screenshot_pdf(self):
        url = f'https://doi.org/{self.doi}'
        async with httpx.AsyncClient(
                timeout=int(os.getenv('TIMEOUT', 600))) as client:
            api_response = await client.post(
                "https://api.zyte.com/v1/extract",
                auth=(os.getenv('ZYTE_API_KEY'), ""),
                json={
                    "url": url,
                    "screenshot": True,
                    "screenshotOptions": {'fullPage': True}
                },
            )
        screenshot: bytes = base64.b64decode(api_response.json()["screenshot"])
        image = Image.open(BytesIO(screenshot))
        pdf_buffer = BytesIO()
        pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=image.size)
        pdf_canvas.drawImage(ImageReader(image), 0, 0)
        pdf_canvas.save()
        pdf_buffer.seek(0)
        return pdf_buffer.read()
