# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PhoneNumberListParams"]


class PhoneNumberListParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination. Use the next_cursor from a previous response."""

    before: str
    """Cursor for backward pagination.

    Use the previous_cursor from a previous response.
    """
