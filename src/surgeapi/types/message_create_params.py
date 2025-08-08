# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.attachment_params import AttachmentParams

__all__ = ["MessageCreateParams", "Conversation", "ConversationContact"]


class MessageCreateParams(TypedDict, total=False):
    conversation: Required[Conversation]
    """Params for selecting or creating a new conversation.

    Either the id or the Contact must be given.
    """

    attachments: Iterable[AttachmentParams]

    body: str
    """The message body."""


class ConversationContact(TypedDict, total=False):
    id: str
    """The unique identifier for an existing contact."""

    first_name: str
    """The contact's first name in case a new contact is created."""

    last_name: str
    """The message's last name in case a new contact is created."""

    phone_number: str
    """The contact's phone number in E.164 format."""


class Conversation(TypedDict, total=False):
    id: str
    """Unique identifier for the object."""

    contact: ConversationContact
    """Params for selecting or creating a new contact for sending a message.

    Either the id or the phone number must be given.
    """
