# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .contact import Contact
from .._models import BaseModel

__all__ = ["RecordingListResponse", "Call"]


class Call(BaseModel):
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


class RecordingListResponse(BaseModel):
    """A call recording"""

    id: str
    """The unique identifier for the recording"""

    call: Call
    """The call that produced this recording"""

    duration: int
    """The duration of the recording in seconds"""
