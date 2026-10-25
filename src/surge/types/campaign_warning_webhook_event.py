# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CampaignWarningWebhookEvent", "Data", "DataFeedback"]


class DataFeedback(BaseModel):
    field: str
    """The stable registration field key"""

    message: str
    """Actionable review feedback"""

    outcome: Literal["warning"]
    """Whether the feedback blocks registration or is a non-blocking warning"""

    suggested_value: Optional[str] = None
    """A suggested replacement value, or null when none is suggested"""


class Data(BaseModel):
    """The data associated with the event"""

    id: str
    """The unique identifier for the campaign"""

    feedback: List[DataFeedback]
    """Customer-visible field-level registration feedback.

    Rejection events may include non-blocking warnings alongside changes-needed
    items.
    """

    status: Literal["in_review"]
    """The public campaign status. Always `in_review` for this event."""


class CampaignWarningWebhookEvent(BaseModel):
    account_id: str
    """The ID of the account in which this event occurred"""

    data: Data
    """The data associated with the event"""

    timestamp: datetime
    """The timestamp when this event occurred, in ISO8601 format"""

    type: Literal["campaign.warning"]
    """The type of the event. Always `campaign.warning` for this event."""
