# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MessageCreateParams",
    "Params",
    "ParamsMessageParamsWithConversation",
    "ParamsMessageParamsWithConversationConversation",
    "ParamsMessageParamsWithConversationConversationContact",
    "ParamsMessageParamsWithConversationAttachment",
    "ParamsSimpleMessageParams",
    "ParamsSimpleMessageParamsAttachment",
]


class MessageCreateParams(TypedDict, total=False):
    params: Required[Params]
    """Payload for creating a message.

    Either an attachment or the body must be given. You can specify the recipient
    either using the 'conversation' parameter or the 'to'/'from' parameters, but not
    both.
    """


class ParamsMessageParamsWithConversationConversationContact(TypedDict, total=False):
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


class ParamsMessageParamsWithConversationConversation(TypedDict, total=False):
    contact: Required[ParamsMessageParamsWithConversationConversationContact]
    """Parameters for creating a contact"""

    phone_number: str
    """The phone number from which to send the message.

    This can be either the phone number in E.164 format or a Surge phone number id.
    """


class ParamsMessageParamsWithConversationAttachment(TypedDict, total=False):
    url: Required[str]
    """The URL of the attachment."""


class ParamsMessageParamsWithConversation(TypedDict, total=False):
    conversation: Required[ParamsMessageParamsWithConversationConversation]
    """Params for selecting or creating a new conversation.

    Either the id or the Contact must be given.
    """

    attachments: Iterable[ParamsMessageParamsWithConversationAttachment]

    body: str
    """The message body."""

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    An optional datetime for scheduling message up to a couple of months in the
    future.
    """


class ParamsSimpleMessageParamsAttachment(TypedDict, total=False):
    url: Required[str]
    """The URL of the attachment."""


_ParamsSimpleMessageParamsReservedKeywords = TypedDict(
    "_ParamsSimpleMessageParamsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ParamsSimpleMessageParams(_ParamsSimpleMessageParamsReservedKeywords, total=False):
    to: Required[str]
    """The recipient's phone number in E.164 format.

    Cannot be used together with 'conversation'.
    """

    attachments: Iterable[ParamsSimpleMessageParamsAttachment]

    body: str
    """The message body."""

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    An optional datetime for scheduling message up to a couple of months in the
    future.
    """


Params: TypeAlias = Union[ParamsMessageParamsWithConversation, ParamsSimpleMessageParams]
