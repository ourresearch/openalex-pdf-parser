import base64
import gzip
import os
from threading import Lock
from urllib.parse import quote

import aioboto3
import botocore
import pdfkit
from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import Chrome

from parse.grobid import GrobidParser

S3_LOCK = Lock()
S3_HTML_BUCKET_NAME = os.getenv('AWS_S3_HTML_BUCKET')

session = aioboto3.Session()


def doi_to_html_key(doi):
    return f'{quote(doi, safe="")}'


# def make_chrome():
#     opts = Options()
#     opts.headless = False
#     return Chrome(options=opts)

#
# CHROME = make_chrome()
# CHROME_LOCK = Lock()


class HTMLController:

    def __init__(self, doi):
        self.doi = doi
        self.parser = None
        self.boto_session = aioboto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

    def clean_html(self, soup):
        for tag in soup.select('[src]'):
            tag.decompose()
        for tag in soup.select('[href]'):
            tag['href'] = ''
        return soup

    async def init(self):
        async with self.boto_session.client('s3') as s3:
            html = await self.get_html(s3)
            # with CHROME_LOCK:
            #     CHROME.get("data:text/html;charset=utf-8,{html_content}".format(
            #         html_content=quote(html)))
            #     output = CHROME.execute_cdp_cmd('Page.printToPDF', {})
            #     pdf = base64.b64decode(output['data'])

            soup = BeautifulSoup(html, parser='lxml', features='lxml')
            cleaned = self.clean_html(soup)
            body = soup.find('body')
            pdf = pdfkit.from_string(str(body) if body else str(cleaned),
                                     options={"load-error-handling": "ignore",
                                              'load-media-error-handling': 'ignore',
                                              'no-images': "",
                                              'disable-javascript': '',
                                              'disable-external-links': '',
                                              'disable-internal-links': '',
                                              'log-level': 'info'})
            # with open(f'./tmp/{quote(self.doi, safe="")}.pdf', 'wb') as f:
            #     f.write(pdf)
            # with open(f'./tmp/{quote(self.doi, safe="")}.html', 'wb') as f:
            #     f.write(html)
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
                return None
