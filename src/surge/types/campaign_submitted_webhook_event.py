# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CampaignSubmittedWebhookEvent", "Data"]


class Data(BaseModel):
    """The data associated with the event"""

    id: str
    """The unique identifier for the campaign"""

    status: Literal["in_review"]
    """The public campaign status. Always `in_review` for this event."""


class CampaignSubmittedWebhookEvent(BaseModel):
    account_id: str
    """The ID of the account in which this event occurred"""

    data: Data
    """The data associated with the event"""

    timestamp: datetime
    """The timestamp when this event occurred, in ISO8601 format"""

    type: Literal["campaign.submitted"]
    """The type of the event. Always `campaign.submitted` for this event."""
