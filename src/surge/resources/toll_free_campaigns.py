# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import toll_free_campaign_list_params, toll_free_campaign_create_params, toll_free_campaign_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.toll_free_campaign import TollFreeCampaign

__all__ = ["TollFreeCampaignsResource", "AsyncTollFreeCampaignsResource"]


class TollFreeCampaignsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TollFreeCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/surgeapi/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TollFreeCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TollFreeCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/surgeapi/python-sdk#with_streaming_response
        """
        return TollFreeCampaignsResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        consent_flows: Iterable[toll_free_campaign_create_params.ConsentFlow],
        description: str,
        message_samples: SequenceNotStr[str],
        phone_number_id: str,
        privacy_policy_url: str,
        terms_and_conditions_url: str,
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
        ],
        includes: List[Literal["age_gated"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TollFreeCampaign:
        """
        Creates a toll-free campaign and submits it for Surge review.

        Args:
          account_id: The account for which the toll-free campaign should be created.

          description: An explanation of how the toll-free number will be used.

          phone_number_id: The toll-free phone number to register.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/toll_free_campaigns", account_id=account_id),
            body=maybe_transform(
                {
                    "consent_flows": consent_flows,
                    "description": description,
                    "message_samples": message_samples,
                    "phone_number_id": phone_number_id,
                    "privacy_policy_url": privacy_policy_url,
                    "terms_and_conditions_url": terms_and_conditions_url,
                    "use_cases": use_cases,
                    "includes": includes,
                },
                toll_free_campaign_create_params.TollFreeCampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TollFreeCampaign,
        )

    def retrieve(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TollFreeCampaign:
        """
        Retrieves a toll-free campaign object.

        Args:
          campaign_id: The ID of the toll-free campaign to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._get(
            path_template("/toll_free_campaigns/{campaign_id}", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TollFreeCampaign,
        )

    def update(
        self,
        campaign_id: str,
        *,
        consent_flows: Iterable[toll_free_campaign_update_params.ConsentFlow] | Omit = omit,
        description: str | Omit = omit,
        includes: List[Literal["age_gated"]] | Omit = omit,
        message_samples: SequenceNotStr[str] | Omit = omit,
        privacy_policy_url: str | Omit = omit,
        terms_and_conditions_url: str | Omit = omit,
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
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TollFreeCampaign:
        """
        Updates a toll-free campaign awaiting customer fixes and re-submits it for Surge
        review. Returns 409 if the campaign is not in an updatable status.

        Args:
          campaign_id: The toll-free campaign ID to update.

          description: An explanation of how the toll-free number will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._patch(
            path_template("/toll_free_campaigns/{campaign_id}", campaign_id=campaign_id),
            body=maybe_transform(
                {
                    "consent_flows": consent_flows,
                    "description": description,
                    "includes": includes,
                    "message_samples": message_samples,
                    "privacy_policy_url": privacy_policy_url,
                    "terms_and_conditions_url": terms_and_conditions_url,
                    "use_cases": use_cases,
                },
                toll_free_campaign_update_params.TollFreeCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TollFreeCampaign,
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
    ) -> SyncCursor[TollFreeCampaign]:
        """
        List all toll-free campaigns for an account with cursor-based pagination.

        Args:
          account_id: The account ID to list toll-free campaigns for.

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
            path_template("/accounts/{account_id}/toll_free_campaigns", account_id=account_id),
            page=SyncCursor[TollFreeCampaign],
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
                    toll_free_campaign_list_params.TollFreeCampaignListParams,
                ),
            ),
            model=TollFreeCampaign,
        )


class AsyncTollFreeCampaignsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTollFreeCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/surgeapi/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTollFreeCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTollFreeCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/surgeapi/python-sdk#with_streaming_response
        """
        return AsyncTollFreeCampaignsResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        consent_flows: Iterable[toll_free_campaign_create_params.ConsentFlow],
        description: str,
        message_samples: SequenceNotStr[str],
        phone_number_id: str,
        privacy_policy_url: str,
        terms_and_conditions_url: str,
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
        ],
        includes: List[Literal["age_gated"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TollFreeCampaign:
        """
        Creates a toll-free campaign and submits it for Surge review.

        Args:
          account_id: The account for which the toll-free campaign should be created.

          description: An explanation of how the toll-free number will be used.

          phone_number_id: The toll-free phone number to register.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/toll_free_campaigns", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "consent_flows": consent_flows,
                    "description": description,
                    "message_samples": message_samples,
                    "phone_number_id": phone_number_id,
                    "privacy_policy_url": privacy_policy_url,
                    "terms_and_conditions_url": terms_and_conditions_url,
                    "use_cases": use_cases,
                    "includes": includes,
                },
                toll_free_campaign_create_params.TollFreeCampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TollFreeCampaign,
        )

    async def retrieve(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TollFreeCampaign:
        """
        Retrieves a toll-free campaign object.

        Args:
          campaign_id: The ID of the toll-free campaign to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._get(
            path_template("/toll_free_campaigns/{campaign_id}", campaign_id=campaign_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TollFreeCampaign,
        )

    async def update(
        self,
        campaign_id: str,
        *,
        consent_flows: Iterable[toll_free_campaign_update_params.ConsentFlow] | Omit = omit,
        description: str | Omit = omit,
        includes: List[Literal["age_gated"]] | Omit = omit,
        message_samples: SequenceNotStr[str] | Omit = omit,
        privacy_policy_url: str | Omit = omit,
        terms_and_conditions_url: str | Omit = omit,
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
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TollFreeCampaign:
        """
        Updates a toll-free campaign awaiting customer fixes and re-submits it for Surge
        review. Returns 409 if the campaign is not in an updatable status.

        Args:
          campaign_id: The toll-free campaign ID to update.

          description: An explanation of how the toll-free number will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._patch(
            path_template("/toll_free_campaigns/{campaign_id}", campaign_id=campaign_id),
            body=await async_maybe_transform(
                {
                    "consent_flows": consent_flows,
                    "description": description,
                    "includes": includes,
                    "message_samples": message_samples,
                    "privacy_policy_url": privacy_policy_url,
                    "terms_and_conditions_url": terms_and_conditions_url,
                    "use_cases": use_cases,
                },
                toll_free_campaign_update_params.TollFreeCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TollFreeCampaign,
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
    ) -> AsyncPaginator[TollFreeCampaign, AsyncCursor[TollFreeCampaign]]:
        """
        List all toll-free campaigns for an account with cursor-based pagination.

        Args:
          account_id: The account ID to list toll-free campaigns for.

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
            path_template("/accounts/{account_id}/toll_free_campaigns", account_id=account_id),
            page=AsyncCursor[TollFreeCampaign],
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
                    toll_free_campaign_list_params.TollFreeCampaignListParams,
                ),
            ),
            model=TollFreeCampaign,
        )


class TollFreeCampaignsResourceWithRawResponse:
    def __init__(self, toll_free_campaigns: TollFreeCampaignsResource) -> None:
        self._toll_free_campaigns = toll_free_campaigns

        self.create = to_raw_response_wrapper(
            toll_free_campaigns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            toll_free_campaigns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            toll_free_campaigns.update,
        )
        self.list = to_raw_response_wrapper(
            toll_free_campaigns.list,
        )


class AsyncTollFreeCampaignsResourceWithRawResponse:
    def __init__(self, toll_free_campaigns: AsyncTollFreeCampaignsResource) -> None:
        self._toll_free_campaigns = toll_free_campaigns

        self.create = async_to_raw_response_wrapper(
            toll_free_campaigns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            toll_free_campaigns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            toll_free_campaigns.update,
        )
        self.list = async_to_raw_response_wrapper(
            toll_free_campaigns.list,
        )


class TollFreeCampaignsResourceWithStreamingResponse:
    def __init__(self, toll_free_campaigns: TollFreeCampaignsResource) -> None:
        self._toll_free_campaigns = toll_free_campaigns

        self.create = to_streamed_response_wrapper(
            toll_free_campaigns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            toll_free_campaigns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            toll_free_campaigns.update,
        )
        self.list = to_streamed_response_wrapper(
            toll_free_campaigns.list,
        )


class AsyncTollFreeCampaignsResourceWithStreamingResponse:
    def __init__(self, toll_free_campaigns: AsyncTollFreeCampaignsResource) -> None:
        self._toll_free_campaigns = toll_free_campaigns

        self.create = async_to_streamed_response_wrapper(
            toll_free_campaigns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            toll_free_campaigns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            toll_free_campaigns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            toll_free_campaigns.list,
        )
