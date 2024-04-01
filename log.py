import logging
from typing import Final

import boto3

logger: Final = logging.getLogger('openalex-pdf-parser')
logging.basicConfig(level=logging.INFO)


def mute_boto_logging():
    libs_to_mum = [
        'boto',
        'boto3',
        'botocore',
        's3transfer'
    ]
    for lib in libs_to_mum:
        logging.getLogger(lib).setLevel(logging.CRITICAL)


mute_boto_logging()
