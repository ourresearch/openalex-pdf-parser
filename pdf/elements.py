from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Author:
    name: str
    aff_ids: list
    is_corresponding: Optional[bool] = None


@dataclass
class Affiliation:
    organization: str
    aff_id: Optional[Union[int, str]]


@dataclass
class AuthorAffiliations:
    name: str
    affiliations: list
    is_corresponding: Optional[bool] = None
