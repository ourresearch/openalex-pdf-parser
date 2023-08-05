import base64
import gzip
import re
import zlib
from io import BytesIO

from bs4 import BeautifulSoup
from grobid_client import Client
import os
from urllib.parse import urljoin

from grobid_client.models import ProcessForm
from tenacity import retry, stop_after_attempt, wait_fixed

from grobid_client.types import File
from grobid_client.api.pdf import process_fulltext_document

from pdf.parser import Parser


class GrobidParser(Parser):
    parser_name = "grobid"

    BASE_URL = os.getenv('GROBID_BASE_URL')

    # BASE_URL = 'https://kermitt2-grobid.hf.space/'

    def __init__(self, pdf_contents):
        base_api_url = GrobidParser.BASE_URL if GrobidParser.BASE_URL.endswith(
            '/api') else urljoin(GrobidParser.BASE_URL, 'api')
        self.client = Client(base_url=base_api_url, timeout=30)
        self.pdf_contents = pdf_contents

    @staticmethod
    def no_authors_output():
        return {"authors": [], "abstract": None, "published_date": None,
                "genre": None, 'references': []}

    @staticmethod
    def cleanup_text(fulltext):
        fulltext = fulltext.replace(
            'GROBID - A machine learning software for extracting information from scholarly documents',
            '')
        return fulltext

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
    def get_grobid_soup(self):
        form = ProcessForm(
            segment_sentences="1",
            include_raw_citations="1",
            include_raw_affiliations="1",
            input_=File(file_name="contents.pdf",
                        payload=BytesIO(self.pdf_contents),
                        mime_type="application/pdf"),
        )
        r = process_fulltext_document.sync_detailed(client=self.client,
                                                    multipart_data=form)
        soup = BeautifulSoup(r.content, parser='lxml', features='lxml')

        if body_tag := soup.select_one('body'):
            if 'HTTP ERROR 503' in body_tag.text:
                raise Exception('503 error from GROBID')
        return soup

    @staticmethod
    def make_ref_dict(ref_tag):
        d = {
            'doi': None,
            'title': None,
            'author': None,
            'volume': None,
            'year': None,
            'journal': None,
            'page': None,
            'raw': None
        }
        if doi_tag := ref_tag.select_one('idno[type="DOI"]'):
            d['doi'] = doi_tag.text.strip()
        if title_tag := ref_tag.select_one('title:not([level="j"])'):
            d['title'] = title_tag.text.strip()
        author = ''
        if first_name_tag := ref_tag.select_one(
                'author forename[type="first"]'):
            author += first_name_tag.text.strip() + ' '
        if middle_name_tag := ref_tag.select_one(
                'author forename[type="middle"]'):
            author += middle_name_tag.text.strip() + ' '
        if last_name_tag := ref_tag.select_one(
                'author surname'):
            author += last_name_tag.text.strip()
        d['author'] = author if author else None
        if journal_tag := ref_tag.select_one('title[level="j"]'):
            d['journal'] = journal_tag.text.strip()
        if year_tag := ref_tag.select_one('date[type="published"]'):
            d['year'] = year_tag.text.strip()
        if volume_tag := ref_tag.select_one('biblscope[unit="volume"]'):
            d['volume'] = volume_tag.text.strip()
        if page_tag := ref_tag.select_one('biblscope[unit="page"]'):
            page_str = None
            start_page = page_tag.get('from')
            end_page = page_tag.get('to')
            if start_page and end_page:
                page_str = f'{start_page} - {end_page}'
            elif start_page:
                page_str = start_page
            elif end_page:
                page_str = end_page
            d['page'] = page_str
        if raw_tag := ref_tag.select_one('note[type="raw_reference"]'):
            d['raw'] = raw_tag.text.strip()
        return d

    def parse(self):
        soup = self.get_grobid_soup()
        body = None
        if body_tag := soup.select_one('body'):
            body = str(body_tag)
        authors = []
        author_tags = soup.select('sourceDesc author')
        universal_affs = []
        for tag in author_tags:
            author = {'name': None, 'affiliations': [],
                      'is_corresponding': tag.get('role', '') == 'corresp'}
            if first_name := tag.select_one('forename[type=first]'):
                last_name = tag.select_one('surname')
                author['name'] = f'{first_name.text} {last_name.text}'
                aff_tags = tag.select('note[type=raw_affiliation]')
                for aff_tag in aff_tags:
                    if label := aff_tag.find('label'):
                        label.decompose()
                    author['affiliations'].append(aff_tag.text.strip())
                authors.append(author)
            elif universal_aff_tag := tag.select_one(
                    'note[type=raw_affiliation]'):
                if label := universal_aff_tag.find('label'):
                    label.decompose()
                universal_affs.append(universal_aff_tag.text)
        for author in authors:
            if not author['affiliations']:
                author['affiliations'].extend(universal_affs)
        abstract = None
        if abstract_tag := soup.select_one('abstract'):
            abstract = abstract_tag.text

        ref_tags = soup.select(
            'div[type=references] listbibl biblstruct')
        refs = [self.make_ref_dict(tag) for tag in ref_tags]
        refs = [ref for ref in refs if ref['doi'] or len([val for val in ref.values() if val]) > 1]
        return {'authors': authors,
                'abstract': self.cleanup_text(abstract) if abstract else None,
                'fulltext': self.cleanup_text(body) if body else None,
                'references': refs,
                'raw': base64.encodebytes(zlib.compress(str(soup).encode())).decode()}
