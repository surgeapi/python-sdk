# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkFollowedWebhookEvent", "Data"]


class Data(BaseModel):
    """The data associated with the event"""

    id: str
    """The unique identifier for the link"""

    message_id: str
    """The unique identifier for the message that contained the link"""

    url: str
    """The original URL that was shortened"""


class LinkFollowedWebhookEvent(BaseModel):
    account_id: str
    """The ID of the account in which this event occurred"""

    data: Data
    """The data associated with the event"""

    timestamp: datetime
    """The timestamp when this event occurred, in ISO8601 format"""

    type: Literal["link.followed"]
    """The type of the event. Always `link.followed` for this event."""
