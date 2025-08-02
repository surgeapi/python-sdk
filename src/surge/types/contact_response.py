# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ContactResponse"]


class ContactResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    email: Optional[str] = None
    """The contact's email address."""

    first_name: Optional[str] = None
    """The contact's first name."""

    last_name: Optional[str] = None
    """The contact's last name."""

    metadata: Optional[Dict[str, str]] = None
    """Set of key-value pairs that will be stored with the object."""

    phone_number: Optional[str] = None
    """The contact's phone number in E.164 format."""
