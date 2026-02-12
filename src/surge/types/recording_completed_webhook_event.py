# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .contact import Contact
from .._models import BaseModel

__all__ = ["RecordingCompletedWebhookEvent", "Data", "DataCall"]


class DataCall(BaseModel):
    """The call that produced this recording"""

    id: str
    """The unique identifier for the call"""

    contact: Contact
    """A contact who has consented to receive messages"""

    duration: int
    """The duration of the call in seconds"""

    initiated_at: datetime
    """When the call was initiated"""

    status: Literal[
        "busy", "canceled", "completed", "failed", "in_progress", "missed", "no_answer", "queued", "ringing"
    ]
    """The status of the call"""


class Data(BaseModel):
    """The data associated with the event"""

    id: str
    """The unique identifier for the recording"""

    call: DataCall
    """The call that produced this recording"""

    duration: int
    """The duration of the recording in seconds"""


class RecordingCompletedWebhookEvent(BaseModel):
    account_id: str
    """The ID of the account in which this event occurred"""

    data: Data
    """The data associated with the event"""

    timestamp: datetime
    """The timestamp when this event occurred, in ISO8601 format"""

    type: Literal["recording.completed"]
    """The type of the event. Always `recording.completed` for this event."""
