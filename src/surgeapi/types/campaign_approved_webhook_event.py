# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CampaignApprovedWebhookEvent", "Data"]


class Data(BaseModel):
    id: str
    """The unique identifier for the campaign"""

    status: Literal["active"]
    """The status of the campaign. Will always be `active` for this event."""


class CampaignApprovedWebhookEvent(BaseModel):
    account_id: str
    """The ID of the account in which this event occurred"""

    data: Data
    """The data associated with the event"""

    type: Literal["campaign.approved"]
    """The type of the event. Always `campaign.approved` for this event."""
