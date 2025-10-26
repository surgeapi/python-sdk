# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .message_params import MessageParams

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    params: Required[MessageParams]
    """Payload for creating a message.

    Either an attachment or the body must be given. You can specify the recipient
    either using the 'conversation' parameter or the 'to'/'from' parameters, but not
    both.
    """
