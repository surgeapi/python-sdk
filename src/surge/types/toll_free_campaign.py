# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .toll_free_campaign_consent_flow import TollFreeCampaignConsentFlow

__all__ = ["TollFreeCampaign"]


class TollFreeCampaign(BaseModel):
    """A toll-free campaign registration for a phone number."""

    id: str
    """The toll-free campaign ID"""

    consent_flows: List[TollFreeCampaignConsentFlow]

    description: Optional[str] = None

    includes: List[Literal["age_gated"]]

    message_samples: List[str]

    phone_number_id: str
    """The toll-free phone number ID"""

    privacy_policy_url: Optional[str] = None

    status: Literal["active", "canceled", "created", "in_review", "rejected"]
    """The current status of the toll-free campaign."""

    terms_and_conditions_url: Optional[str] = None

    use_cases: List[
        Literal[
            "two_factor_authentication",
            "account_notification",
            "customer_care",
            "charity",
            "delivery_notification",
            "fraud_alert",
            "event",
            "higher_education",
            "k12_education",
            "marketing",
            "polling_voting",
            "political",
            "public_service_announcement",
            "security_alert",
        ]
    ]
