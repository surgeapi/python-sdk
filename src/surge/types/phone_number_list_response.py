# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .phone_number import PhoneNumber

__all__ = ["PhoneNumberListResponse", "Pagination"]


class Pagination(BaseModel):
    """Cursor-based pagination information"""

    next_cursor: Optional[str] = None
    """Cursor for the next page of results. Null if there is no next page."""

    previous_cursor: Optional[str] = None
    """Cursor for the previous page of results. Null if there is no previous page."""


class PhoneNumberListResponse(BaseModel):
    """A paginated list of phone numbers"""

    data: List[PhoneNumber]
    """The list of phone numbers"""

    pagination: Pagination
    """Cursor-based pagination information"""
