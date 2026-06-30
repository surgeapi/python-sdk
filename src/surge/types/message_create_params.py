# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MessageCreateParams",
    "MessageParamsWithConversation",
    "MessageParamsWithConversationConversation",
    "MessageParamsWithConversationConversationContact",
    "MessageParamsWithConversationAttachment",
    "MessageParamsWithConversationSettings",
    "SimpleMessageParams",
    "SimpleMessageParamsAttachment",
    "SimpleMessageParamsSettings",
]


class MessageParamsWithConversation(TypedDict, total=False):
    conversation: Required[MessageParamsWithConversationConversation]
    """Params for selecting or creating a new conversation.

    Either the id or the Contact must be given.
    """

    attachments: Iterable[MessageParamsWithConversationAttachment]

    body: str
    """The message body."""

    metadata: Dict[str, str]
    """Set of key-value pairs that will be stored with the object."""

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    An optional datetime for scheduling message up to a couple of months in the
    future.
    """

    settings: MessageParamsWithConversationSettings
    """Per-message setting overrides."""


class MessageParamsWithConversationConversationContact(TypedDict, total=False):
    """Parameters for creating a contact"""

    phone_number: Required[str]
    """The contact's phone number in E.164 format."""

    email: str
    """The contact's email address."""

    first_name: str
    """The contact's first name."""

    last_name: str
    """The contact's last name."""

    metadata: Dict[str, str]
    """Set of key-value pairs that will be stored with the object."""


class MessageParamsWithConversationConversation(TypedDict, total=False):
    """Params for selecting or creating a new conversation.

    Either the id or the Contact must be given.
    """

    contact: Required[MessageParamsWithConversationConversationContact]
    """Parameters for creating a contact"""

    phone_number: str
    """The phone number from which to send the message.

    This can be either the phone number in E.164 format or a Surge phone number id.
    """


class MessageParamsWithConversationAttachment(TypedDict, total=False):
    """Params for creating an attachment"""

    url: Required[str]
    """The URL of the attachment."""


class MessageParamsWithConversationSettings(TypedDict, total=False):
    """Per-message setting overrides."""

    link_shortening: Literal["enabled", "disabled"]
    """Override link shortening for this message."""


class SimpleMessageParams(TypedDict, total=False):
    to: Required[str]
    """The recipient's phone number in E.164 format.

    Cannot be used together with 'conversation'.
    """

    attachments: Iterable[SimpleMessageParamsAttachment]

    body: str
    """The message body."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """The sender's phone number in E.164 format or phone number ID.

    If omitted, uses the account's default phone number. Cannot be used together
    with 'conversation'.
    """

    metadata: Dict[str, str]
    """Set of key-value pairs that will be stored with the object."""

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    An optional datetime for scheduling message up to a couple of months in the
    future.
    """

    settings: SimpleMessageParamsSettings
    """Per-message setting overrides."""


class SimpleMessageParamsAttachment(TypedDict, total=False):
    """Params for creating an attachment"""

    url: Required[str]
    """The URL of the attachment."""


class SimpleMessageParamsSettings(TypedDict, total=False):
    """Per-message setting overrides."""

    link_shortening: Literal["enabled", "disabled"]
    """Override link shortening for this message."""


MessageCreateParams: TypeAlias = Union[MessageParamsWithConversation, SimpleMessageParams]
