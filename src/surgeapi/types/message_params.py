# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .contact_params import ContactParams

__all__ = [
    "MessageParams",
    "UnionMember0",
    "UnionMember0Conversation",
    "UnionMember0Attachment",
    "UnionMember1",
    "UnionMember1Attachment",
]


class UnionMember0Conversation(TypedDict, total=False):
    contact: Required[ContactParams]
    """Parameters for creating a contact"""

    phone_number: str
    """The phone number from which to send the message.

    This can be either the phone number in E.164 format or a Surge phone number id.
    """


class UnionMember0Attachment(TypedDict, total=False):
    url: Required[str]
    """The URL of the attachment."""


class UnionMember0(TypedDict, total=False):
    conversation: Required[UnionMember0Conversation]
    """Params for selecting or creating a new conversation.

    Either the id or the Contact must be given.
    """

    attachments: Iterable[UnionMember0Attachment]

    body: str
    """The message body."""

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    An optional datetime for scheduling message up to a couple of months in the
    future.
    """


class UnionMember1Attachment(TypedDict, total=False):
    url: Required[str]
    """The URL of the attachment."""


_UnionMember1ReservedKeywords = TypedDict(
    "_UnionMember1ReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class UnionMember1(_UnionMember1ReservedKeywords, total=False):
    to: Required[str]
    """The recipient's phone number in E.164 format.

    Cannot be used together with 'conversation'.
    """

    attachments: Iterable[UnionMember1Attachment]

    body: str
    """The message body."""

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    An optional datetime for scheduling message up to a couple of months in the
    future.
    """


MessageParams: TypeAlias = Union[UnionMember0, UnionMember1]
