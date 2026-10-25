# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "TollFreeCampaignUpdateParams",
    "ConsentFlow",
    "ConsentFlowUnionMember0",
    "ConsentFlowUnionMember1",
    "ConsentFlowUnionMember1Screenshot",
    "ConsentFlowUnionMember2",
    "ConsentFlowUnionMember3",
]


class TollFreeCampaignUpdateParams(TypedDict, total=False):
    consent_flows: Iterable[ConsentFlow]

    description: str
    """An explanation of how the toll-free number will be used."""

    includes: List[Literal["age_gated"]]

    message_samples: SequenceNotStr[str]

    privacy_policy_url: str

    terms_and_conditions_url: str

    use_cases: List[
        Literal[
            "two_factor_authentication",
            "account_notification",
            "customer_care",
            "charity",
            "delivery_notification",
            "fraud_alert",
            "event",
            "higher_education",
            "k12_education",
            "marketing",
            "polling_voting",
            "political",
            "public_service_announcement",
            "security_alert",
        ]
    ]


class ConsentFlowUnionMember0(TypedDict, total=False):
    script: Required[str]

    type: Required[Literal["verbal"]]


class ConsentFlowUnionMember1Screenshot(TypedDict, total=False):
    reason: Required[Literal["behind_login", "under_construction", "other"]]

    urls: Required[SequenceNotStr[str]]

    reason_other: str


class ConsentFlowUnionMember1(TypedDict, total=False):
    owner: Required[Literal["brand", "platform"]]

    type: Required[Literal["web_form"]]

    form_url: str

    screenshot: ConsentFlowUnionMember1Screenshot


class ConsentFlowUnionMember2(TypedDict, total=False):
    file_urls: Required[SequenceNotStr[str]]

    type: Required[Literal["text"]]

    keywords: SequenceNotStr[str]


class ConsentFlowUnionMember3(TypedDict, total=False):
    file_urls: Required[SequenceNotStr[str]]

    type: Required[Literal["paper_form"]]


ConsentFlow: TypeAlias = Union[
    ConsentFlowUnionMember0, ConsentFlowUnionMember1, ConsentFlowUnionMember2, ConsentFlowUnionMember3
]
