# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.contact import Contact

__all__ = ["MessageCreateResponse", "Attachment", "Conversation"]


class Attachment(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    type: Optional[str] = None
    """The type of attachment."""

    url: Optional[str] = None
    """The URL of the attachment."""


class Conversation(BaseModel):
    id: str
    """Unique identifier for the object."""

    contact: Contact
    """A contact who has consented to receive messages"""


class MessageCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    attachments: Optional[List[Attachment]] = None

    body: Optional[str] = None
    """The message body."""

    conversation: Optional[Conversation] = None
    """A conversation with a Contact"""
