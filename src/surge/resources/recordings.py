# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import recording_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursor, AsyncCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.recording_list_response import RecordingListResponse
from ..types.recording_delete_response import RecordingDeleteResponse
from ..types.recording_get_file_response import RecordingGetFileResponse
from ..types.recording_retrieve_response import RecordingRetrieveResponse

__all__ = ["RecordingsResource", "AsyncRecordingsResource"]


class RecordingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/surgeapi/python-sdk#accessing-raw-response-data-eg-headers
        """
        return RecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/surgeapi/python-sdk#with_streaming_response
        """
        return RecordingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingRetrieveResponse:
        """
        Retrieves a Recording object.

        Args:
          id: The ID of the recording to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/recordings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingRetrieveResponse,
        )

    def list(
        self,
        account_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[RecordingListResponse]:
        """
        List all recordings for an account with cursor-based pagination.

        Args:
          account_id: The account ID to list recordings for.

          after: Cursor for forward pagination. Use the next_cursor from a previous response.

          before: Cursor for backward pagination. Use the previous_cursor from a previous
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/recordings", account_id=account_id),
            page=SyncCursor[RecordingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                    },
                    recording_list_params.RecordingListParams,
                ),
            ),
            model=RecordingListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingDeleteResponse:
        """Deletes a recording.

        The recording file will be removed from storage
        asynchronously.

        Args:
          id: The ID of the recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/recordings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingDeleteResponse,
        )

    def get_file(
        self,
        recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingGetFileResponse:
        """Redirects to a signed URL where the recording audio file can be downloaded.

        URL
        is short-lived, so redirect should be followed immediately.

        Args:
          recording_id: The ID of the recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return self._get(
            path_template("/recordings/{recording_id}/file", recording_id=recording_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingGetFileResponse,
        )


class AsyncRecordingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/surgeapi/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/surgeapi/python-sdk#with_streaming_response
        """
        return AsyncRecordingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingRetrieveResponse:
        """
        Retrieves a Recording object.

        Args:
          id: The ID of the recording to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/recordings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingRetrieveResponse,
        )

    def list(
        self,
        account_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RecordingListResponse, AsyncCursor[RecordingListResponse]]:
        """
        List all recordings for an account with cursor-based pagination.

        Args:
          account_id: The account ID to list recordings for.

          after: Cursor for forward pagination. Use the next_cursor from a previous response.

          before: Cursor for backward pagination. Use the previous_cursor from a previous
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/recordings", account_id=account_id),
            page=AsyncCursor[RecordingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                    },
                    recording_list_params.RecordingListParams,
                ),
            ),
            model=RecordingListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingDeleteResponse:
        """Deletes a recording.

        The recording file will be removed from storage
        asynchronously.

        Args:
          id: The ID of the recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/recordings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingDeleteResponse,
        )

    async def get_file(
        self,
        recording_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingGetFileResponse:
        """Redirects to a signed URL where the recording audio file can be downloaded.

        URL
        is short-lived, so redirect should be followed immediately.

        Args:
          recording_id: The ID of the recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_id:
            raise ValueError(f"Expected a non-empty value for `recording_id` but received {recording_id!r}")
        return await self._get(
            path_template("/recordings/{recording_id}/file", recording_id=recording_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingGetFileResponse,
        )


class RecordingsResourceWithRawResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

        self.retrieve = to_raw_response_wrapper(
            recordings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            recordings.list,
        )
        self.delete = to_raw_response_wrapper(
            recordings.delete,
        )
        self.get_file = to_raw_response_wrapper(
            recordings.get_file,
        )


class AsyncRecordingsResourceWithRawResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

        self.retrieve = async_to_raw_response_wrapper(
            recordings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            recordings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            recordings.delete,
        )
        self.get_file = async_to_raw_response_wrapper(
            recordings.get_file,
        )


class RecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

        self.retrieve = to_streamed_response_wrapper(
            recordings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            recordings.list,
        )
        self.delete = to_streamed_response_wrapper(
            recordings.delete,
        )
        self.get_file = to_streamed_response_wrapper(
            recordings.get_file,
        )


class AsyncRecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

        self.retrieve = async_to_streamed_response_wrapper(
            recordings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            recordings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            recordings.delete,
        )
        self.get_file = async_to_streamed_response_wrapper(
            recordings.get_file,
        )
