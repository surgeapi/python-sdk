# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .contact import Contact
from .._models import BaseModel

__all__ = ["VoicemailReceivedWebhookEvent", "Data", "DataCall"]


class DataCall(BaseModel):
    """The call that resulted in this voicemail"""

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

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The E.164 phone number of the caller"""

    phone_number_id: Optional[str] = None
    """The Surge phone number ID (e.g. pn\\__...)"""

    to: Optional[str] = None
    """The E.164 phone number of the callee"""


class Data(BaseModel):
    """The data associated with the event"""

    id: str
    """The unique identifier for the voicemail"""

    call: DataCall
    """The call that resulted in this voicemail"""

    duration: int
    """The duration of the voicemail in seconds"""

    recording_id: str
    """The unique identifier for the recording"""


class VoicemailReceivedWebhookEvent(BaseModel):
    account_id: str
    """The ID of the account in which this event occurred"""

    data: Data
    """The data associated with the event"""

    timestamp: datetime
    """The timestamp when this event occurred, in ISO8601 format"""

    type: Literal["voicemail.received"]
    """The type of the event. Always `voicemail.received` for this event."""
