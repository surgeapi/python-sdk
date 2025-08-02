# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TokenCreateTokenResponse"]


class TokenCreateTokenResponse(BaseModel):
    token: Optional[str] = None
    """The created token."""
