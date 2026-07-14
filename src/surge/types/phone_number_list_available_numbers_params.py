# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhoneNumberListAvailableNumbersParams"]


class PhoneNumberListAvailableNumbersParams(TypedDict, total=False):
    type: Required[Literal["local", "toll_free"]]
    """Whether to search for local or toll-free numbers."""

    after: str
    """Cursor for forward pagination. Use the next_cursor from a previous response."""

    area_code: str
    """Filter by 3-digit area code."""

    before: str
    """Cursor for backward pagination.

    Use the previous_cursor from a previous response.
    """

    country: Literal["US", "CA"]
    """ISO country code to search in."""
