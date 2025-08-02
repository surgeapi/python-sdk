# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhoneNumberCreateParams"]


class PhoneNumberCreateParams(TypedDict, total=False):
    type: Required[Literal["local", "toll_free"]]
    """Whether the phone number is local or toll-free"""

    area_code: str
    """The desired area code for this phone number."""
