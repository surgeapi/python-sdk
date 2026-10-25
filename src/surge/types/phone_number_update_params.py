# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    campaign_id: str
    """Campaign ID to attach this number to (`cpn_...`)."""

    metadata: Dict[str, str]
    """Set of key-value pairs that will be stored with the object."""

    name: str
    """A human-readable name for the phone number."""
