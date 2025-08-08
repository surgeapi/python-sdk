# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountCreateResponse"]


class AccountCreateResponse(BaseModel):
    id: str
    """The account ID"""

    name: str
    """The name of the account"""

    call_forwarding_number: Optional[str] = None
    """The phone number to forward calls to"""

    time_zone: Optional[str] = None
    """The time zone for the account"""
