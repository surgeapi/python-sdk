# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .verification import Verification

__all__ = ["VerificationCheckResponse"]


class VerificationCheckResponse(BaseModel):
    result: Optional[Literal["ok", "incorrect", "exhausted", "expired", "already_verified"]] = None
    """The result of the code check.

    This result will affect the status code of the response:

    - ok: 200
    - incorrect: 422
    - exhausted: 422
    - expired: 422
    - already_verified: 409
    """

    verification: Optional[Verification] = None
    """A phone number verification"""
