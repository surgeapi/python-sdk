# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "TollFreeCampaignConsentFlow",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember2Screenshot",
    "UnionMember3",
    "Type",
]


class UnionMember0(BaseModel):
    script: str

    type: Literal["verbal"]


class UnionMember1(BaseModel):
    form_url: str

    type: Literal["web_form"]


class UnionMember2Screenshot(BaseModel):
    reason: Literal["behind_login", "under_construction", "other"]

    reason_other: Optional[str] = None


class UnionMember2(BaseModel):
    screenshot: UnionMember2Screenshot

    type: Literal["web_form"]


class UnionMember3(BaseModel):
    type: Literal["text"]

    keywords: Optional[List[str]] = None


class Type(BaseModel):
    type: Literal["paper_form"]


TollFreeCampaignConsentFlow: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3, Type]
