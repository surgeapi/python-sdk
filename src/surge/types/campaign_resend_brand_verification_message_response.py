# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CampaignResendBrandVerificationMessageResponse"]


class CampaignResendBrandVerificationMessageResponse(BaseModel):
    """Response when a brand verification OTP send has been enqueued"""

    status: Literal["enqueued"]
    """Indicates the OTP send job was enqueued successfully."""
