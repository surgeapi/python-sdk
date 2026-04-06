# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AudienceCreateResponse"]


class AudienceCreateResponse(BaseModel):
    """A group of contacts used for targeting messages."""

    id: str
    """Unique identifier for the object."""

    name: str
    """A name to identify this Audience. This name will only be visible within Surge."""
