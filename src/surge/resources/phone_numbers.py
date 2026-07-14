# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    phone_number_list_params,
    phone_number_update_params,
    phone_number_purchase_params,
    phone_number_list_available_numbers_params,
)
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
from ..types.phone_number import PhoneNumber
from ..types.phone_number_list_available_numbers_response import PhoneNumberListAvailableNumbersResponse

__all__ = ["PhoneNumbersResource", "AsyncPhoneNumbersResource"]


class PhoneNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/surgeapi/python-sdk#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/surgeapi/python-sdk#with_streaming_response
        """
        return PhoneNumbersResourceWithStreamingResponse(self)

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
    ) -> PhoneNumber:
        """
        Retrieves a PhoneNumber object.

        Args:
          id: The ID of the phone number to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/phone_numbers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumber,
        )

    def update(
        self,
        id: str,
        *,
        campaign_id: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumber:
        """
        Updates a phone number's details.

        Args:
          id: The ID of the phone number to update.

          campaign_id: Campaign ID to attach this number to (`cpn_...`).

          name: A human-readable name for the phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/phone_numbers/{id}", id=id),
            body=maybe_transform(
                {
                    "campaign_id": campaign_id,
                    "name": name,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumber,
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
    ) -> SyncCursor[PhoneNumber]:
        """
        List all phone numbers for an account with cursor-based pagination.

        Args:
          account_id: The account ID to list phone numbers for.

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
            path_template("/accounts/{account_id}/phone_numbers", account_id=account_id),
            page=SyncCursor[PhoneNumber],
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
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            model=PhoneNumber,
        )

    def list_available_numbers(
        self,
        account_id: str,
        *,
        type: Literal["local", "toll_free"],
        after: str | Omit = omit,
        area_code: str | Omit = omit,
        before: str | Omit = omit,
        country: Literal["US", "CA"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[PhoneNumberListAvailableNumbersResponse]:
        """
        Browse purchasable phone numbers from Surge inventory before buying.

        Pagination cursors are always null for now.

        Args:
          account_id: The account ID to list available phone numbers for.

          type: Whether to search for local or toll-free numbers.

          after: Cursor for forward pagination. Use the next_cursor from a previous response.

          area_code: Filter by 3-digit area code.

          before: Cursor for backward pagination. Use the previous_cursor from a previous
              response.

          country: ISO country code to search in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/available_phone_numbers", account_id=account_id),
            page=SyncCursor[PhoneNumberListAvailableNumbersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "after": after,
                        "area_code": area_code,
                        "before": before,
                        "country": country,
                    },
                    phone_number_list_available_numbers_params.PhoneNumberListAvailableNumbersParams,
                ),
            ),
            model=PhoneNumberListAvailableNumbersResponse,
        )

    def purchase(
        self,
        account_id: str,
        *,
        area_code: str | Omit = omit,
        latitude: float | Omit = omit,
        longitude: float | Omit = omit,
        name: str | Omit = omit,
        type: Literal["local", "toll_free"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumber:
        """Purchase a new phone number for the account.

        You can specify search criteria or
        let the system select a random number.

        Args:
          account_id: The account for which the phone number should be created.

          area_code: The desired area code for this phone number. If provided without type, the type
              will be inferred.

          latitude: Latitude to search for nearby phone numbers. Must be used with longitude. If
              provided without type, type will be inferred as 'local'.

          longitude: Longitude to search for nearby phone numbers. Must be used with latitude. If
              provided without type, type will be inferred as 'local'.

          name: A human-readable name for the phone number. If not provided, defaults to the
              formatted phone number.

          type: Whether the phone number is local or toll-free. Can be omitted if area_code or
              latitude/longitude are provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/phone_numbers", account_id=account_id),
            body=maybe_transform(
                {
                    "area_code": area_code,
                    "latitude": latitude,
                    "longitude": longitude,
                    "name": name,
                    "type": type,
                },
                phone_number_purchase_params.PhoneNumberPurchaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumber,
        )

    def release(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumber:
        """
        Releases a phone number from the account.

        Args:
          id: The ID of the phone number to release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/phone_numbers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumber,
        )


class AsyncPhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/surgeapi/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/surgeapi/python-sdk#with_streaming_response
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self)

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
    ) -> PhoneNumber:
        """
        Retrieves a PhoneNumber object.

        Args:
          id: The ID of the phone number to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/phone_numbers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumber,
        )

    async def update(
        self,
        id: str,
        *,
        campaign_id: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumber:
        """
        Updates a phone number's details.

        Args:
          id: The ID of the phone number to update.

          campaign_id: Campaign ID to attach this number to (`cpn_...`).

          name: A human-readable name for the phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/phone_numbers/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "campaign_id": campaign_id,
                    "name": name,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumber,
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
    ) -> AsyncPaginator[PhoneNumber, AsyncCursor[PhoneNumber]]:
        """
        List all phone numbers for an account with cursor-based pagination.

        Args:
          account_id: The account ID to list phone numbers for.

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
            path_template("/accounts/{account_id}/phone_numbers", account_id=account_id),
            page=AsyncCursor[PhoneNumber],
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
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            model=PhoneNumber,
        )

    def list_available_numbers(
        self,
        account_id: str,
        *,
        type: Literal["local", "toll_free"],
        after: str | Omit = omit,
        area_code: str | Omit = omit,
        before: str | Omit = omit,
        country: Literal["US", "CA"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PhoneNumberListAvailableNumbersResponse, AsyncCursor[PhoneNumberListAvailableNumbersResponse]]:
        """
        Browse purchasable phone numbers from Surge inventory before buying.

        Pagination cursors are always null for now.

        Args:
          account_id: The account ID to list available phone numbers for.

          type: Whether to search for local or toll-free numbers.

          after: Cursor for forward pagination. Use the next_cursor from a previous response.

          area_code: Filter by 3-digit area code.

          before: Cursor for backward pagination. Use the previous_cursor from a previous
              response.

          country: ISO country code to search in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/available_phone_numbers", account_id=account_id),
            page=AsyncCursor[PhoneNumberListAvailableNumbersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "after": after,
                        "area_code": area_code,
                        "before": before,
                        "country": country,
                    },
                    phone_number_list_available_numbers_params.PhoneNumberListAvailableNumbersParams,
                ),
            ),
            model=PhoneNumberListAvailableNumbersResponse,
        )

    async def purchase(
        self,
        account_id: str,
        *,
        area_code: str | Omit = omit,
        latitude: float | Omit = omit,
        longitude: float | Omit = omit,
        name: str | Omit = omit,
        type: Literal["local", "toll_free"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumber:
        """Purchase a new phone number for the account.

        You can specify search criteria or
        let the system select a random number.

        Args:
          account_id: The account for which the phone number should be created.

          area_code: The desired area code for this phone number. If provided without type, the type
              will be inferred.

          latitude: Latitude to search for nearby phone numbers. Must be used with longitude. If
              provided without type, type will be inferred as 'local'.

          longitude: Longitude to search for nearby phone numbers. Must be used with latitude. If
              provided without type, type will be inferred as 'local'.

          name: A human-readable name for the phone number. If not provided, defaults to the
              formatted phone number.

          type: Whether the phone number is local or toll-free. Can be omitted if area_code or
              latitude/longitude are provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/phone_numbers", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "area_code": area_code,
                    "latitude": latitude,
                    "longitude": longitude,
                    "name": name,
                    "type": type,
                },
                phone_number_purchase_params.PhoneNumberPurchaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumber,
        )

    async def release(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumber:
        """
        Releases a phone number from the account.

        Args:
          id: The ID of the phone number to release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/phone_numbers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumber,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = to_raw_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.list_available_numbers = to_raw_response_wrapper(
            phone_numbers.list_available_numbers,
        )
        self.purchase = to_raw_response_wrapper(
            phone_numbers.purchase,
        )
        self.release = to_raw_response_wrapper(
            phone_numbers.release,
        )


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = async_to_raw_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.list_available_numbers = async_to_raw_response_wrapper(
            phone_numbers.list_available_numbers,
        )
        self.purchase = async_to_raw_response_wrapper(
            phone_numbers.purchase,
        )
        self.release = async_to_raw_response_wrapper(
            phone_numbers.release,
        )


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = to_streamed_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.list_available_numbers = to_streamed_response_wrapper(
            phone_numbers.list_available_numbers,
        )
        self.purchase = to_streamed_response_wrapper(
            phone_numbers.purchase,
        )
        self.release = to_streamed_response_wrapper(
            phone_numbers.release,
        )


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = async_to_streamed_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.list_available_numbers = async_to_streamed_response_wrapper(
            phone_numbers.list_available_numbers,
        )
        self.purchase = async_to_streamed_response_wrapper(
            phone_numbers.purchase,
        )
        self.release = async_to_streamed_response_wrapper(
            phone_numbers.release,
        )
