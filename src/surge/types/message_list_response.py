# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .message import Message
from .._models import BaseModel

__all__ = ["MessageListResponse", "Pagination"]


class Pagination(BaseModel):
    """Cursor-based pagination information"""

    next_cursor: Optional[str] = None
    """Cursor for the next page of results. Null if there is no next page."""

    previous_cursor: Optional[str] = None
    """Cursor for the previous page of results. Null if there is no previous page."""


class MessageListResponse(BaseModel):
    """A paginated list of messages"""

    data: List[Message]
    """The list of messages"""

    pagination: Pagination
    """Cursor-based pagination information"""
