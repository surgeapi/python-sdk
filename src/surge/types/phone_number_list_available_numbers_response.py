# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberListAvailableNumbersResponse"]


class PhoneNumberListAvailableNumbersResponse(BaseModel):
    """A phone number available for purchase from Surge inventory"""

    country: Literal["US", "CA"]
    """ISO country code for the phone number"""

    number: str
    """The phone number in E.164 format"""

    type: Literal["local", "toll_free"]
    """Whether the phone number is local or toll-free"""
