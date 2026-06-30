# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    campaign_id: str
    """Campaign ID to attach this number to (`cpn_...`)."""

    name: str
    """A human-readable name for the phone number."""
