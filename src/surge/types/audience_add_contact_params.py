# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AudienceAddContactParams"]


class AudienceAddContactParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the contact to add.

    The contact must belong to the same account as the audience.
    """
