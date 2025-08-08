# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the account"""

    call_forwarding_number: str
    """The phone number to forward calls to"""

    time_zone: Optional[str]
    """The time zone for the account"""
