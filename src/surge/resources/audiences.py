# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import audience_create_params, audience_add_contact_params, audience_list_contacts_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.contact import Contact
from ..types.audience_create_response import AudienceCreateResponse

__all__ = ["AudiencesResource", "AsyncAudiencesResource"]


class AudiencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/surgeapi/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/surgeapi/python-sdk#with_streaming_response
        """
        return AudiencesResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceCreateResponse:
        """
        Creates a new audience.

        Args:
          account_id: The account for which the audience should be created.

          name: The audience name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/audiences", account_id=account_id),
            body=maybe_transform({"name": name}, audience_create_params.AudienceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudienceCreateResponse,
        )

    def add_contact(
        self,
        audience_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """
        Adds an existing contact to a manual audience.

        Args:
          audience_id: The audience ID to add the contact to.

          id: The ID of the contact to add. The contact must belong to the same account as the
              audience.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return self._post(
            path_template("/audiences/{audience_id}/contacts", audience_id=audience_id),
            body=maybe_transform({"id": id}, audience_add_contact_params.AudienceAddContactParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def list_contacts(
        self,
        audience_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Contact]:
        """List all contacts in an audience with cursor-based pagination.

        The account is
        inferred from the audience.

        Args:
          audience_id: The audience ID to list contacts for.

          after: Cursor for forward pagination. Use the next_cursor from a previous response.

          before: Cursor for backward pagination. Use the previous_cursor from a previous
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return self._get_api_list(
            path_template("/audiences/{audience_id}/contacts", audience_id=audience_id),
            page=SyncCursor[Contact],
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
                    audience_list_contacts_params.AudienceListContactsParams,
                ),
            ),
            model=Contact,
        )


class AsyncAudiencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/surgeapi/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/surgeapi/python-sdk#with_streaming_response
        """
        return AsyncAudiencesResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceCreateResponse:
        """
        Creates a new audience.

        Args:
          account_id: The account for which the audience should be created.

          name: The audience name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/audiences", account_id=account_id),
            body=await async_maybe_transform({"name": name}, audience_create_params.AudienceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudienceCreateResponse,
        )

    async def add_contact(
        self,
        audience_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """
        Adds an existing contact to a manual audience.

        Args:
          audience_id: The audience ID to add the contact to.

          id: The ID of the contact to add. The contact must belong to the same account as the
              audience.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return await self._post(
            path_template("/audiences/{audience_id}/contacts", audience_id=audience_id),
            body=await async_maybe_transform({"id": id}, audience_add_contact_params.AudienceAddContactParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )

    def list_contacts(
        self,
        audience_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Contact, AsyncCursor[Contact]]:
        """List all contacts in an audience with cursor-based pagination.

        The account is
        inferred from the audience.

        Args:
          audience_id: The audience ID to list contacts for.

          after: Cursor for forward pagination. Use the next_cursor from a previous response.

          before: Cursor for backward pagination. Use the previous_cursor from a previous
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return self._get_api_list(
            path_template("/audiences/{audience_id}/contacts", audience_id=audience_id),
            page=AsyncCursor[Contact],
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
                    audience_list_contacts_params.AudienceListContactsParams,
                ),
            ),
            model=Contact,
        )


class AudiencesResourceWithRawResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.create = to_raw_response_wrapper(
            audiences.create,
        )
        self.add_contact = to_raw_response_wrapper(
            audiences.add_contact,
        )
        self.list_contacts = to_raw_response_wrapper(
            audiences.list_contacts,
        )


class AsyncAudiencesResourceWithRawResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.create = async_to_raw_response_wrapper(
            audiences.create,
        )
        self.add_contact = async_to_raw_response_wrapper(
            audiences.add_contact,
        )
        self.list_contacts = async_to_raw_response_wrapper(
            audiences.list_contacts,
        )


class AudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.create = to_streamed_response_wrapper(
            audiences.create,
        )
        self.add_contact = to_streamed_response_wrapper(
            audiences.add_contact,
        )
        self.list_contacts = to_streamed_response_wrapper(
            audiences.list_contacts,
        )


class AsyncAudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.create = async_to_streamed_response_wrapper(
            audiences.create,
        )
        self.add_contact = async_to_streamed_response_wrapper(
            audiences.add_contact,
        )
        self.list_contacts = async_to_streamed_response_wrapper(
            audiences.list_contacts,
        )
