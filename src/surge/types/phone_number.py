# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumber"]


class PhoneNumber(BaseModel):
    """A phone number that can be used to send and receive messages and calls"""

    id: str
    """Unique identifier for the phone number"""

    campaign_id: Optional[str] = None
    """The unique identifier of the campaign this phone number is attached to, if any"""

    number: str
    """The phone number in E.164 format"""

    type: Literal["local", "short_code", "toll_free"]
    """Whether the phone number is local, toll-free, or short code"""
