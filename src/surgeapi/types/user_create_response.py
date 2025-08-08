# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserCreateResponse"]


class UserCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    first_name: Optional[str] = None
    """The user's first name."""

    last_name: Optional[str] = None
    """The user's last name."""

    metadata: Optional[object] = None
    """Set of key-value pairs that will be stored with the user."""

    photo_url: Optional[str] = None
    """URL of a photo to be used as the user's avatar."""
