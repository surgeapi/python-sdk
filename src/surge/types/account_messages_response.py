# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountMessagesResponse", "Attachment", "Conversation", "ConversationContact", "ConversationPhoneNumber"]


class Attachment(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    type: Optional[str] = None
    """The type of attachment."""

    url: Optional[str] = None
    """The URL of the attachment."""


class ConversationContact(BaseModel):
    id: str
    """Unique identifier for the object."""

    phone_number: str
    """The contact's phone number in E.164 format."""

    first_name: Optional[str] = None
    """The contact's first name."""

    last_name: Optional[str] = None
    """The contact's last name."""


class ConversationPhoneNumber(BaseModel):
    id: str
    """Unique identifier for the phone number"""

    number: str
    """The canonical format of the phone number."""

    type: Literal["local", "toll_free", "short_code", "demo"]
    """Whether the phone number is local, toll-free, or short code"""


class Conversation(BaseModel):
    id: str
    """Unique identifier for the object."""

    contact: ConversationContact
    """A contact who has consented to receive messages"""

    phone_number: Optional[ConversationPhoneNumber] = None
    """This is the phone number tied to the Surge account."""


class AccountMessagesResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    attachments: Optional[List[Attachment]] = None

    body: Optional[str] = None
    """The message body."""

    conversation: Optional[Conversation] = None
    """A conversation with a Contact"""
