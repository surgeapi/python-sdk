# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..types import (
    account_users_params,
    account_blasts_params,
    account_create_params,
    account_update_params,
    account_contacts_params,
    account_messages_params,
    account_campaigns_params,
    account_phone_numbers_params,
    account_retrieve_status_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user_response import UserResponse
from ..types.account_response import AccountResponse
from ..types.contact_response import ContactResponse
from ..types.attachment_params import AttachmentParams
from ..types.account_blasts_response import AccountBlastsResponse
from ..types.account_messages_response import AccountMessagesResponse
from ..types.account_campaigns_response import AccountCampaignsResponse
from ..types.account_phone_numbers_response import AccountPhoneNumbersResponse
from ..types.account_retrieve_status_response import AccountRetrieveStatusResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/surge-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/surge-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        brand_name: Optional[str] | NotGiven = NOT_GIVEN,
        organization: account_create_params.Organization | NotGiven = NOT_GIVEN,
        time_zone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountResponse:
        """
        Creates a new Account within the calling Platform.

        Args:
          name: The name of the account that will be visible for your internal organizational
              purposes. This will also be the default public-facing brand name unless you also
              set a `brand_name`, but otherwise the account name will never be displayed
              anywhere outside of Surge HQ, and may include your ID for the account or
              anything else that may help you.

          brand_name: The name by which the people this account communicates with know it. If not
              provided, this will match the name field.

          organization: The legal entity on whose behalf the account will be operated.

          time_zone: This is the time zone in which the account is headquartered. This time zone may
              be used for compliance with TCPA restrictions on when messages may be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "brand_name": brand_name,
                    "organization": organization,
                    "time_zone": time_zone,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    def update(
        self,
        id: str,
        *,
        brand_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: account_update_params.Organization | NotGiven = NOT_GIVEN,
        time_zone: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountResponse:
        """
        Updates an Account

        Args:
          brand_name: The name by which the people this account communicates with know it. If not
              provided, this will match the name field.

          name: The name of the account that will be visible for your internal organizational
              purposes. This will also be the default public-facing brand name unless you also
              set a `brand_name`, but otherwise the account name will never be displayed
              anywhere outside of Surge HQ, and may include your ID for the account or
              anything else that may help you.

          organization: The legal entity on whose behalf the account will be operated.

          time_zone: The time zone for the account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/accounts/{id}",
            body=maybe_transform(
                {
                    "brand_name": brand_name,
                    "name": name,
                    "organization": organization,
                    "time_zone": time_zone,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    def blasts(
        self,
        account_id: str,
        *,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        contacts: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        segments: List[str] | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        to: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountBlastsResponse:
        """Sends a Blast.

        Args:
          body: The message body.

          contacts: Deprecated.

        Use `to` instead.

          name: Optional name for the blast.

          segments: Deprecated. Use `to` instead.

          send_at: When to send the blast. If not provided, sends immediately.

          to: List of recipients to whom the blast should be sent. This can be a combination
              of contact IDs, segment IDs, and phone numbers.

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
                    "to": to,
                },
                account_blasts_params.AccountBlastsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountBlastsResponse,
        )

    def campaigns(
        self,
        account_id: str,
        *,
        consent_flow: str,
        description: str,
        message_samples: List[str],
        privacy_policy_url: str,
        use_cases: List[
            Literal[
                "account_notification",
                "customer_care",
                "delivery_notification",
                "fraud_alert",
                "higher_education",
                "marketing",
                "polling_voting",
                "public_service_announcement",
                "security_alert",
                "two_factor_authentication",
            ]
        ],
        volume: Literal["high", "low"],
        includes: List[Literal["links", "phone_numbers", "age_gated", "direct_lending"]] | NotGiven = NOT_GIVEN,
        link_sample: str | NotGiven = NOT_GIVEN,
        terms_and_conditions_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCampaignsResponse:
        """
        Creates a campaign to register account to send text messages.

        Args:
          consent_flow: A string explaining the method through which end users will opt in to receive
              messages from the brand. Typically this should include URLs for opt-in forms or
              screenshots that might be helpful in explaining the flow to someone unfamiliar
              with the organization's purpose.

          description: An explanation of the organization's purpose and how it will be using text
              messaging to accomplish that purpose.

          message_samples: An array of 2-5 strings with examples of the messages that will be sent from
              this campaign. Typically the first sample should be a compliance message like
              `You are now opted in to messages from {brand name}. Frequency varies. Msg&data rates apply. Reply STOP to opt out.`
              These samples don't necessarily need to be the only templates that will be used
              for the campaign, but they should reflect the purpose of the messages that will
              be sent. Any variable content can be reflected by wrapping it in square brackets
              like `[customer name]`.

          privacy_policy_url: The URL of the privacy policy for the brand in question. This may be a shared
              privacy policy if it's the policy that is displayed to end users when they opt
              in to messaging.

          use_cases: A list containing 1-5 types of messages that will be sent with this campaign.

              The following use cases are typically available to all brands:

              - `account_notification` - For sending reminders, alerts, and general
                account-related notifications like booking confirmations or appointment
                reminders.
              - `customer_care` - For account support, troubleshooting, and general customer
                service communication.
              - `delivery_notification` - For notifying customers about the status of product
                or service deliveries.
              - `fraud_alert` - For warning customers about suspicious or potentially
                fraudulent activity.
              - `higher_education` - For messaging related to colleges, universities, and
                school districts outside of K–12.
              - `marketing` - For promotional or advertising messages intended to market
                products or services.
              - `polling_voting` - For conducting surveys, polls, or voting-related messaging.
              - `public_service_announcement` - For raising awareness about social issues or
                important public information.
              - `security_alert` - For alerts related to potential security breaches or
                compromised systems requiring user action.
              - `two_factor_authentication` - For sending one-time passwords or verification
                codes for login or password reset.

              For access to special use cases not shown here, reach out to support@surge.app.

          volume:
              This will be one of the following:

              - `low` - The campaign will be allowed to send up to 2000 SMS segments to
                T-Mobile customers each day. In this case your platform will be charged for
                the setup fee for a low volume number upon receipt of the API request.
              - `high` - The campaign will be allowed to send up to 200k SMS segments to
                T-Mobile customers each day, depending on the trust score assigned by The
                Campaign Registry. Your platform will be charged for the setup fee for a high
                volume number upon receipt of the API request, and phone numbers will be
                charged as high volume numbers going forward.

          includes: A list of properties that this campaign should include. These properties can be
              any of the following values:

              - `links` - whether the campaign might send links in messages
              - `phone_numbers` - whether the campaign might send phone numbers in messages
              - `age_gated` - whether the campaign contains age gated content (controlled
                substances or adult content)
              - `direct_lending` - whether the campaign contains content related to direct
                lending or other loan arrangements

          link_sample: A sample link that might be sent by this campaign. If links from other domains
              are sent through this campaign, they are much more likely to be filtered by the
              carriers. If link shortening is enabled for the account, the link shortener URL
              will be used instead of what is provided. Reach out to support if you would like
              to disable automatic link shortening.

          terms_and_conditions_url: The URL of the terms and conditions presented to end users when they opt in to
              messaging. These terms and conditions may be shared among all of a platform's
              customers if they're the terms that are presented to end users when they opt in
              to messaging.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/campaigns",
            body=maybe_transform(
                {
                    "consent_flow": consent_flow,
                    "description": description,
                    "message_samples": message_samples,
                    "privacy_policy_url": privacy_policy_url,
                    "use_cases": use_cases,
                    "volume": volume,
                    "includes": includes,
                    "link_sample": link_sample,
                    "terms_and_conditions_url": terms_and_conditions_url,
                },
                account_campaigns_params.AccountCampaignsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCampaignsResponse,
        )

    def contacts(
        self,
        account_id: str,
        *,
        phone_number: str,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactResponse:
        """
        Creates a new Contact object.

        Args:
          phone_number: The contact's phone number in E.164 format.

          email: The contact's email address.

          first_name: The contact's first name.

          last_name: The contact's last name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/contacts",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                },
                account_contacts_params.AccountContactsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    @overload
    def messages(
        self,
        account_id: str,
        *,
        conversation: account_messages_params.Variant0Conversation,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMessagesResponse:
        """
        Creates and enqueues a new message to be sent.

        Messages are always sent asynchronously. When you hit this endpoint, the message
        will be created within Surge's system and enqueued for sending, and then the id
        for the new message will be returned. When the message is actually sent, a
        `message.sent` webhook event will be triggered and sent to any webhook endpoints
        that you have subscribed to this event type. Then a `message.delivered` webhook
        event will be triggered when the carrier sends us a delivery receipt.

        By default all messages will be sent immediately. If you would like to schedule
        sending for some time up to 60 days in the future, you can do that by providing
        a value for the `send_at` field. This should be formatted as an ISO8601 datetime
        like `2028-10-14T18:06:00Z`.

        You must include either a `body` or `attachments` field (or both) in the request
        body. The `body` field should contain the text of the message you want to send,
        and the `attachments` field should be an array of objects with a `url` field
        pointing to the file you want to attach. Surge will download these files and
        send them as attachments in the message.

        You can provide either a `conversation` object or a `to` field to specify the
        intended recipient of the message, but an error will be returned if both fields
        are provided. Similarly the `from` field cannot be used together with the
        `conversation` field, and `conversation.phone_number` should be specified
        instead.

        Args:
          conversation: Params for selecting or creating a new conversation. Either the id or the
              Contact must be given.

          body: The message body.

          send_at: An optional datetime for scheduling message up to a couple of months in the
              future.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def messages(
        self,
        account_id: str,
        *,
        to: str,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMessagesResponse:
        """
        Creates and enqueues a new message to be sent.

        Messages are always sent asynchronously. When you hit this endpoint, the message
        will be created within Surge's system and enqueued for sending, and then the id
        for the new message will be returned. When the message is actually sent, a
        `message.sent` webhook event will be triggered and sent to any webhook endpoints
        that you have subscribed to this event type. Then a `message.delivered` webhook
        event will be triggered when the carrier sends us a delivery receipt.

        By default all messages will be sent immediately. If you would like to schedule
        sending for some time up to 60 days in the future, you can do that by providing
        a value for the `send_at` field. This should be formatted as an ISO8601 datetime
        like `2028-10-14T18:06:00Z`.

        You must include either a `body` or `attachments` field (or both) in the request
        body. The `body` field should contain the text of the message you want to send,
        and the `attachments` field should be an array of objects with a `url` field
        pointing to the file you want to attach. Surge will download these files and
        send them as attachments in the message.

        You can provide either a `conversation` object or a `to` field to specify the
        intended recipient of the message, but an error will be returned if both fields
        are provided. Similarly the `from` field cannot be used together with the
        `conversation` field, and `conversation.phone_number` should be specified
        instead.

        Args:
          to: The recipient's phone number in E.164 format. Cannot be used together with
              'conversation'.

          body: The message body.

          from_: The sender's phone number in E.164 format or phone number ID. If omitted, uses
              the account's default phone number. Cannot be used together with 'conversation'.

          send_at: An optional datetime for scheduling message up to a couple of months in the
              future.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["conversation"], ["to"])
    def messages(
        self,
        account_id: str,
        *,
        conversation: account_messages_params.Variant0Conversation | NotGiven = NOT_GIVEN,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMessagesResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/messages",
            body=maybe_transform(
                {
                    "conversation": conversation,
                    "attachments": attachments,
                    "body": body,
                    "send_at": send_at,
                    "to": to,
                    "from_": from_,
                },
                account_messages_params.AccountMessagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountMessagesResponse,
        )

    def phone_numbers(
        self,
        account_id: str,
        *,
        type: Literal["local", "toll_free"],
        area_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountPhoneNumbersResponse:
        """
        Create a new phone number for the account.

        Args:
          type: Whether the phone number is local or toll-free

          area_code: The desired area code for this phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/phone_numbers",
            body=maybe_transform(
                {
                    "type": type,
                    "area_code": area_code,
                },
                account_phone_numbers_params.AccountPhoneNumbersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountPhoneNumbersResponse,
        )

    def retrieve_status(
        self,
        account_id: str,
        *,
        capabilities: List[Literal["local_messaging"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveStatusResponse:
        """
        Check an account's status and capabilities

        Args:
          capabilities: capabilities about which to check the status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"capabilities": capabilities}, account_retrieve_status_params.AccountRetrieveStatusParams
                ),
            ),
            cast_to=AccountRetrieveStatusResponse,
        )

    def users(
        self,
        account_id: str,
        *,
        first_name: str,
        last_name: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        photo_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResponse:
        """
        Creates a new User object.

        Args:
          first_name: The user's first name.

          last_name: The user's last name.

          metadata: Set of key-value pairs that will be stored with the user.

          photo_url: URL of a photo to be used as the user's avatar.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/users",
            body=maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                    "photo_url": photo_url,
                },
                account_users_params.AccountUsersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/surge-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/surge-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        brand_name: Optional[str] | NotGiven = NOT_GIVEN,
        organization: account_create_params.Organization | NotGiven = NOT_GIVEN,
        time_zone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountResponse:
        """
        Creates a new Account within the calling Platform.

        Args:
          name: The name of the account that will be visible for your internal organizational
              purposes. This will also be the default public-facing brand name unless you also
              set a `brand_name`, but otherwise the account name will never be displayed
              anywhere outside of Surge HQ, and may include your ID for the account or
              anything else that may help you.

          brand_name: The name by which the people this account communicates with know it. If not
              provided, this will match the name field.

          organization: The legal entity on whose behalf the account will be operated.

          time_zone: This is the time zone in which the account is headquartered. This time zone may
              be used for compliance with TCPA restrictions on when messages may be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounts",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "brand_name": brand_name,
                    "organization": organization,
                    "time_zone": time_zone,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    async def update(
        self,
        id: str,
        *,
        brand_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: account_update_params.Organization | NotGiven = NOT_GIVEN,
        time_zone: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountResponse:
        """
        Updates an Account

        Args:
          brand_name: The name by which the people this account communicates with know it. If not
              provided, this will match the name field.

          name: The name of the account that will be visible for your internal organizational
              purposes. This will also be the default public-facing brand name unless you also
              set a `brand_name`, but otherwise the account name will never be displayed
              anywhere outside of Surge HQ, and may include your ID for the account or
              anything else that may help you.

          organization: The legal entity on whose behalf the account will be operated.

          time_zone: The time zone for the account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/accounts/{id}",
            body=await async_maybe_transform(
                {
                    "brand_name": brand_name,
                    "name": name,
                    "organization": organization,
                    "time_zone": time_zone,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    async def blasts(
        self,
        account_id: str,
        *,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        contacts: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        segments: List[str] | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        to: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountBlastsResponse:
        """Sends a Blast.

        Args:
          body: The message body.

          contacts: Deprecated.

        Use `to` instead.

          name: Optional name for the blast.

          segments: Deprecated. Use `to` instead.

          send_at: When to send the blast. If not provided, sends immediately.

          to: List of recipients to whom the blast should be sent. This can be a combination
              of contact IDs, segment IDs, and phone numbers.

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
                    "to": to,
                },
                account_blasts_params.AccountBlastsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountBlastsResponse,
        )

    async def campaigns(
        self,
        account_id: str,
        *,
        consent_flow: str,
        description: str,
        message_samples: List[str],
        privacy_policy_url: str,
        use_cases: List[
            Literal[
                "account_notification",
                "customer_care",
                "delivery_notification",
                "fraud_alert",
                "higher_education",
                "marketing",
                "polling_voting",
                "public_service_announcement",
                "security_alert",
                "two_factor_authentication",
            ]
        ],
        volume: Literal["high", "low"],
        includes: List[Literal["links", "phone_numbers", "age_gated", "direct_lending"]] | NotGiven = NOT_GIVEN,
        link_sample: str | NotGiven = NOT_GIVEN,
        terms_and_conditions_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCampaignsResponse:
        """
        Creates a campaign to register account to send text messages.

        Args:
          consent_flow: A string explaining the method through which end users will opt in to receive
              messages from the brand. Typically this should include URLs for opt-in forms or
              screenshots that might be helpful in explaining the flow to someone unfamiliar
              with the organization's purpose.

          description: An explanation of the organization's purpose and how it will be using text
              messaging to accomplish that purpose.

          message_samples: An array of 2-5 strings with examples of the messages that will be sent from
              this campaign. Typically the first sample should be a compliance message like
              `You are now opted in to messages from {brand name}. Frequency varies. Msg&data rates apply. Reply STOP to opt out.`
              These samples don't necessarily need to be the only templates that will be used
              for the campaign, but they should reflect the purpose of the messages that will
              be sent. Any variable content can be reflected by wrapping it in square brackets
              like `[customer name]`.

          privacy_policy_url: The URL of the privacy policy for the brand in question. This may be a shared
              privacy policy if it's the policy that is displayed to end users when they opt
              in to messaging.

          use_cases: A list containing 1-5 types of messages that will be sent with this campaign.

              The following use cases are typically available to all brands:

              - `account_notification` - For sending reminders, alerts, and general
                account-related notifications like booking confirmations or appointment
                reminders.
              - `customer_care` - For account support, troubleshooting, and general customer
                service communication.
              - `delivery_notification` - For notifying customers about the status of product
                or service deliveries.
              - `fraud_alert` - For warning customers about suspicious or potentially
                fraudulent activity.
              - `higher_education` - For messaging related to colleges, universities, and
                school districts outside of K–12.
              - `marketing` - For promotional or advertising messages intended to market
                products or services.
              - `polling_voting` - For conducting surveys, polls, or voting-related messaging.
              - `public_service_announcement` - For raising awareness about social issues or
                important public information.
              - `security_alert` - For alerts related to potential security breaches or
                compromised systems requiring user action.
              - `two_factor_authentication` - For sending one-time passwords or verification
                codes for login or password reset.

              For access to special use cases not shown here, reach out to support@surge.app.

          volume:
              This will be one of the following:

              - `low` - The campaign will be allowed to send up to 2000 SMS segments to
                T-Mobile customers each day. In this case your platform will be charged for
                the setup fee for a low volume number upon receipt of the API request.
              - `high` - The campaign will be allowed to send up to 200k SMS segments to
                T-Mobile customers each day, depending on the trust score assigned by The
                Campaign Registry. Your platform will be charged for the setup fee for a high
                volume number upon receipt of the API request, and phone numbers will be
                charged as high volume numbers going forward.

          includes: A list of properties that this campaign should include. These properties can be
              any of the following values:

              - `links` - whether the campaign might send links in messages
              - `phone_numbers` - whether the campaign might send phone numbers in messages
              - `age_gated` - whether the campaign contains age gated content (controlled
                substances or adult content)
              - `direct_lending` - whether the campaign contains content related to direct
                lending or other loan arrangements

          link_sample: A sample link that might be sent by this campaign. If links from other domains
              are sent through this campaign, they are much more likely to be filtered by the
              carriers. If link shortening is enabled for the account, the link shortener URL
              will be used instead of what is provided. Reach out to support if you would like
              to disable automatic link shortening.

          terms_and_conditions_url: The URL of the terms and conditions presented to end users when they opt in to
              messaging. These terms and conditions may be shared among all of a platform's
              customers if they're the terms that are presented to end users when they opt in
              to messaging.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/campaigns",
            body=await async_maybe_transform(
                {
                    "consent_flow": consent_flow,
                    "description": description,
                    "message_samples": message_samples,
                    "privacy_policy_url": privacy_policy_url,
                    "use_cases": use_cases,
                    "volume": volume,
                    "includes": includes,
                    "link_sample": link_sample,
                    "terms_and_conditions_url": terms_and_conditions_url,
                },
                account_campaigns_params.AccountCampaignsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCampaignsResponse,
        )

    async def contacts(
        self,
        account_id: str,
        *,
        phone_number: str,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactResponse:
        """
        Creates a new Contact object.

        Args:
          phone_number: The contact's phone number in E.164 format.

          email: The contact's email address.

          first_name: The contact's first name.

          last_name: The contact's last name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/contacts",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                },
                account_contacts_params.AccountContactsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    @overload
    async def messages(
        self,
        account_id: str,
        *,
        conversation: account_messages_params.Variant0Conversation,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMessagesResponse:
        """
        Creates and enqueues a new message to be sent.

        Messages are always sent asynchronously. When you hit this endpoint, the message
        will be created within Surge's system and enqueued for sending, and then the id
        for the new message will be returned. When the message is actually sent, a
        `message.sent` webhook event will be triggered and sent to any webhook endpoints
        that you have subscribed to this event type. Then a `message.delivered` webhook
        event will be triggered when the carrier sends us a delivery receipt.

        By default all messages will be sent immediately. If you would like to schedule
        sending for some time up to 60 days in the future, you can do that by providing
        a value for the `send_at` field. This should be formatted as an ISO8601 datetime
        like `2028-10-14T18:06:00Z`.

        You must include either a `body` or `attachments` field (or both) in the request
        body. The `body` field should contain the text of the message you want to send,
        and the `attachments` field should be an array of objects with a `url` field
        pointing to the file you want to attach. Surge will download these files and
        send them as attachments in the message.

        You can provide either a `conversation` object or a `to` field to specify the
        intended recipient of the message, but an error will be returned if both fields
        are provided. Similarly the `from` field cannot be used together with the
        `conversation` field, and `conversation.phone_number` should be specified
        instead.

        Args:
          conversation: Params for selecting or creating a new conversation. Either the id or the
              Contact must be given.

          body: The message body.

          send_at: An optional datetime for scheduling message up to a couple of months in the
              future.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def messages(
        self,
        account_id: str,
        *,
        to: str,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMessagesResponse:
        """
        Creates and enqueues a new message to be sent.

        Messages are always sent asynchronously. When you hit this endpoint, the message
        will be created within Surge's system and enqueued for sending, and then the id
        for the new message will be returned. When the message is actually sent, a
        `message.sent` webhook event will be triggered and sent to any webhook endpoints
        that you have subscribed to this event type. Then a `message.delivered` webhook
        event will be triggered when the carrier sends us a delivery receipt.

        By default all messages will be sent immediately. If you would like to schedule
        sending for some time up to 60 days in the future, you can do that by providing
        a value for the `send_at` field. This should be formatted as an ISO8601 datetime
        like `2028-10-14T18:06:00Z`.

        You must include either a `body` or `attachments` field (or both) in the request
        body. The `body` field should contain the text of the message you want to send,
        and the `attachments` field should be an array of objects with a `url` field
        pointing to the file you want to attach. Surge will download these files and
        send them as attachments in the message.

        You can provide either a `conversation` object or a `to` field to specify the
        intended recipient of the message, but an error will be returned if both fields
        are provided. Similarly the `from` field cannot be used together with the
        `conversation` field, and `conversation.phone_number` should be specified
        instead.

        Args:
          to: The recipient's phone number in E.164 format. Cannot be used together with
              'conversation'.

          body: The message body.

          from_: The sender's phone number in E.164 format or phone number ID. If omitted, uses
              the account's default phone number. Cannot be used together with 'conversation'.

          send_at: An optional datetime for scheduling message up to a couple of months in the
              future.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["conversation"], ["to"])
    async def messages(
        self,
        account_id: str,
        *,
        conversation: account_messages_params.Variant0Conversation | NotGiven = NOT_GIVEN,
        attachments: Iterable[AttachmentParams] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountMessagesResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/messages",
            body=await async_maybe_transform(
                {
                    "conversation": conversation,
                    "attachments": attachments,
                    "body": body,
                    "send_at": send_at,
                    "to": to,
                    "from_": from_,
                },
                account_messages_params.AccountMessagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountMessagesResponse,
        )

    async def phone_numbers(
        self,
        account_id: str,
        *,
        type: Literal["local", "toll_free"],
        area_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountPhoneNumbersResponse:
        """
        Create a new phone number for the account.

        Args:
          type: Whether the phone number is local or toll-free

          area_code: The desired area code for this phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/phone_numbers",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "area_code": area_code,
                },
                account_phone_numbers_params.AccountPhoneNumbersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountPhoneNumbersResponse,
        )

    async def retrieve_status(
        self,
        account_id: str,
        *,
        capabilities: List[Literal["local_messaging"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveStatusResponse:
        """
        Check an account's status and capabilities

        Args:
          capabilities: capabilities about which to check the status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"capabilities": capabilities}, account_retrieve_status_params.AccountRetrieveStatusParams
                ),
            ),
            cast_to=AccountRetrieveStatusResponse,
        )

    async def users(
        self,
        account_id: str,
        *,
        first_name: str,
        last_name: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        photo_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResponse:
        """
        Creates a new User object.

        Args:
          first_name: The user's first name.

          last_name: The user's last name.

          metadata: Set of key-value pairs that will be stored with the user.

          photo_url: URL of a photo to be used as the user's avatar.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/users",
            body=await async_maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                    "photo_url": photo_url,
                },
                account_users_params.AccountUsersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.blasts = to_raw_response_wrapper(
            accounts.blasts,
        )
        self.campaigns = to_raw_response_wrapper(
            accounts.campaigns,
        )
        self.contacts = to_raw_response_wrapper(
            accounts.contacts,
        )
        self.messages = to_raw_response_wrapper(
            accounts.messages,
        )
        self.phone_numbers = to_raw_response_wrapper(
            accounts.phone_numbers,
        )
        self.retrieve_status = to_raw_response_wrapper(
            accounts.retrieve_status,
        )
        self.users = to_raw_response_wrapper(
            accounts.users,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.blasts = async_to_raw_response_wrapper(
            accounts.blasts,
        )
        self.campaigns = async_to_raw_response_wrapper(
            accounts.campaigns,
        )
        self.contacts = async_to_raw_response_wrapper(
            accounts.contacts,
        )
        self.messages = async_to_raw_response_wrapper(
            accounts.messages,
        )
        self.phone_numbers = async_to_raw_response_wrapper(
            accounts.phone_numbers,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            accounts.retrieve_status,
        )
        self.users = async_to_raw_response_wrapper(
            accounts.users,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.blasts = to_streamed_response_wrapper(
            accounts.blasts,
        )
        self.campaigns = to_streamed_response_wrapper(
            accounts.campaigns,
        )
        self.contacts = to_streamed_response_wrapper(
            accounts.contacts,
        )
        self.messages = to_streamed_response_wrapper(
            accounts.messages,
        )
        self.phone_numbers = to_streamed_response_wrapper(
            accounts.phone_numbers,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            accounts.retrieve_status,
        )
        self.users = to_streamed_response_wrapper(
            accounts.users,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.blasts = async_to_streamed_response_wrapper(
            accounts.blasts,
        )
        self.campaigns = async_to_streamed_response_wrapper(
            accounts.campaigns,
        )
        self.contacts = async_to_streamed_response_wrapper(
            accounts.contacts,
        )
        self.messages = async_to_streamed_response_wrapper(
            accounts.messages,
        )
        self.phone_numbers = async_to_streamed_response_wrapper(
            accounts.phone_numbers,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            accounts.retrieve_status,
        )
        self.users = async_to_streamed_response_wrapper(
            accounts.users,
        )
