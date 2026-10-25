# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserCreateTokenParams"]


class UserCreateTokenParams(TypedDict, total=False):
    duration_seconds: int
    """For how many seconds the token should be accepted. Defaults to 15 minutes."""

    read_only: bool
    """Restrict the token to viewing embedded conversations and unread counts.

    Sending messages, changing read state, editing contacts, and calling are
    disabled. Defaults to false. Preserve this value when refreshing the token;
    changing access mode requires reloading the embed.
    """
