# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberAttachedToCampaignWebhookEvent", "Data"]


class Data(BaseModel):
    """The data associated with the event"""

    id: str
    """The unique identifier for the phone number"""

    campaign_id: str
    """The unique identifier of the campaign this phone number is attached to"""

    number: str
    """The phone number in E.164 format"""

    type: Literal["local", "short_code", "toll_free"]
    """Whether the phone number is local, toll-free, or short code"""


class PhoneNumberAttachedToCampaignWebhookEvent(BaseModel):
    account_id: str
    """The ID of the account in which this event occurred"""

    data: Data
    """The data associated with the event"""

    timestamp: datetime
    """The timestamp when this event occurred, in ISO8601 format"""

    type: Literal["phone_number.attached_to_campaign"]
    """The type of the event.

    Always `phone_number.attached_to_campaign` for this event.
    """
