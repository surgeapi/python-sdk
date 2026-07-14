# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumber", "Campaign"]


class Campaign(BaseModel):
    """Campaign attachment details for a domestic local phone number"""

    id: str
    """The unique identifier of the campaign this phone number is attached to"""

    attachment_status: Literal["attached", "attachment_pending", "detached", "detachment_pending"]
    """The current campaign attachment status for this phone number."""


class PhoneNumber(BaseModel):
    """A phone number that can be used to send and receive messages and calls"""

    id: str
    """Unique identifier for the phone number"""

    campaign: Optional[Campaign] = None
    """Campaign attachment details for a domestic local phone number"""

    campaign_id: Optional[str] = None
    """Deprecated.

    The unique identifier of the campaign this phone number is attached to, if any
    """

    name: Optional[str] = None
    """A human-readable name for the phone number"""

    number: str
    """The phone number in E.164 format"""

    type: Literal["local", "short_code", "toll_free"]
    """Whether the phone number is local, toll-free, or short code"""
