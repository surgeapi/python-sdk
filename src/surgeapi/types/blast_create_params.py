# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import TypedDict

from .shared_params.attachment_params import AttachmentParams

__all__ = ["BlastCreateParams"]


class BlastCreateParams(TypedDict, total=False):
    attachments: Iterable[AttachmentParams]

    body: str
    """The message body."""

    contacts: List[str]
    """List of contact IDs to send the blast to."""

    name: str
    """Optional name for the blast."""

    segments: List[str]
    """List of segment IDs to send the blast to."""

    send_at: str
    """When to send the blast. If not provided, sends immediately."""
