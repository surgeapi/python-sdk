# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.attachment_params import AttachmentParams

__all__ = ["BlastBlastsParams"]


class BlastBlastsParams(TypedDict, total=False):
    attachments: Iterable[AttachmentParams]

    body: str
    """The message body."""

    contacts: List[str]
    """Deprecated. Use `to` instead."""

    name: str
    """Optional name for the blast."""

    segments: List[str]
    """Deprecated. Use `to` instead."""

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When to send the blast. If not provided, sends immediately."""

    to: List[str]
    """List of recipients to whom the blast should be sent.

    This can be a combination of contact IDs, segment IDs, and phone numbers.
    """
