# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .shared.error import Error

__all__ = ["AttachmentGetFileResponse"]


class AttachmentGetFileResponse(BaseModel):
    """An error response"""

    error: Error
    """An error response"""
