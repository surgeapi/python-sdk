# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..types import blast_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.blast_create_response import BlastCreateResponse
from ..types.shared_params.attachment_params import AttachmentParams

__all__ = ["BlastsResource", "AsyncBlastsResource"]


class BlastsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/surge-python#accessing-raw-response-data-eg-headers
        """
        return BlastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/surge-python#with_streaming_response
        """
        return BlastsResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        contacts: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        segments: List[str] | NotGiven = NOT_GIVEN,
        send_at: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlastCreateResponse:
        """
        Sends a Blast.

        Args:
          body: The message body.

          contacts: List of contact IDs to send the blast to.

          name: Optional name for the blast.

          segments: List of segment IDs to send the blast to.

          send_at: When to send the blast. If not provided, sends immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/blasts",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "body": body,
                    "contacts": contacts,
                    "name": name,
                    "segments": segments,
                    "send_at": send_at,
                },
                blast_create_params.BlastCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlastCreateResponse,
        )


class AsyncBlastsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlastsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/surge-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/surge-python#with_streaming_response
        """
        return AsyncBlastsResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        contacts: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        segments: List[str] | NotGiven = NOT_GIVEN,
        send_at: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlastCreateResponse:
        """
        Sends a Blast.

        Args:
          body: The message body.

          contacts: List of contact IDs to send the blast to.

          name: Optional name for the blast.

          segments: List of segment IDs to send the blast to.

          send_at: When to send the blast. If not provided, sends immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/blasts",
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "body": body,
                    "contacts": contacts,
                    "name": name,
                    "segments": segments,
                    "send_at": send_at,
                },
                blast_create_params.BlastCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlastCreateResponse,
        )


class BlastsResourceWithRawResponse:
    def __init__(self, blasts: BlastsResource) -> None:
        self._blasts = blasts

        self.create = to_raw_response_wrapper(
            blasts.create,
        )


class AsyncBlastsResourceWithRawResponse:
    def __init__(self, blasts: AsyncBlastsResource) -> None:
        self._blasts = blasts

        self.create = async_to_raw_response_wrapper(
            blasts.create,
        )


class BlastsResourceWithStreamingResponse:
    def __init__(self, blasts: BlastsResource) -> None:
        self._blasts = blasts

        self.create = to_streamed_response_wrapper(
            blasts.create,
        )


class AsyncBlastsResourceWithStreamingResponse:
    def __init__(self, blasts: AsyncBlastsResource) -> None:
        self._blasts = blasts

        self.create = async_to_streamed_response_wrapper(
            blasts.create,
        )
