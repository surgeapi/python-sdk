# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from surge import Surge, AsyncSurge
from surge.types import (
    AccountResponse,
    AccountUsersResponse,
    AccountBlastsResponse,
    AccountContactsResponse,
    AccountMessagesResponse,
    AccountCampaignsResponse,
    AccountPhoneNumbersResponse,
    AccountRetrieveStatusResponse,
)
from tests.utils import assert_matches_type
from surge._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create(self, client: Surge) -> None:
        account = client.accounts.create(
            name="Account #2840 - DT Precision Auto",
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create_with_all_params(self, client: Surge) -> None:
        account = client.accounts.create(
            name="Account #2840 - DT Precision Auto",
            brand_name="DT Precision Auto",
            organization={
                "address": {
                    "country": "US",
                    "line1": "2640 Huron St",
                    "line2": None,
                    "locality": "Los Angeles",
                    "name": "DT Precision Auto",
                    "postal_code": "90065",
                    "region": "CA",
                },
                "contact": {
                    "email": "dom@dtprecisionauto.com",
                    "first_name": "Dominic",
                    "last_name": "Toretto",
                    "phone_number": "+13235556439",
                    "title": "other",
                    "title_other": "Owner",
                },
                "country": "US",
                "email": "dom@dtprecisionauto.com",
                "identifier": "123456789",
                "identifier_type": "ein",
                "industry": "automotive",
                "mobile_number": "+13235556439",
                "regions_of_operation": ["usa_and_canada"],
                "registered_name": "DT Precision Auto LLC",
                "stock_exchange": None,
                "stock_symbol": None,
                "type": "llc",
                "website": "https://dtprecisionauto.com",
            },
            time_zone="America/Los_Angeles",
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_create(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.create(
            name="Account #2840 - DT Precision Auto",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_create(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.create(
            name="Account #2840 - DT Precision Auto",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_update(self, client: Surge) -> None:
        account = client.accounts.update(
            id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_update_with_all_params(self, client: Surge) -> None:
        account = client.accounts.update(
            id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
            brand_name="DT Precision Auto",
            name="D·T Precision Auto Shop",
            organization={
                "address": {
                    "country": "US",
                    "line1": "2640 Huron St",
                    "line2": None,
                    "locality": "Los Angeles",
                    "name": "DT Precision Auto",
                    "postal_code": "90065",
                    "region": "CA",
                },
                "contact": {
                    "email": "dom@dtprecisionauto.com",
                    "first_name": "Dominic",
                    "last_name": "Toretto",
                    "phone_number": "+13235556439",
                    "title": "other",
                    "title_other": "Owner",
                },
                "country": "US",
                "email": "dom@dtprecisionauto.com",
                "identifier": "123456789",
                "identifier_type": "ein",
                "industry": "automotive",
                "mobile_number": "+13235556439",
                "regions_of_operation": ["usa_and_canada"],
                "registered_name": "DT Precision Auto LLC",
                "stock_exchange": None,
                "stock_symbol": None,
                "type": "llc",
                "website": "https://dtprecisionauto.com",
            },
            time_zone="America/Los_Angeles",
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_update(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.update(
            id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_update(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.update(
            id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_update(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_blasts(self, client: Surge) -> None:
        account = client.accounts.blasts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(AccountBlastsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_blasts_with_all_params(self, client: Surge) -> None:
        account = client.accounts.blasts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            attachments=[{"url": "https://example.com/image.jpg"}],
            body="Join us for our grand opening!",
            contacts=["ctc_01jxwtp1vse91twb5bj977gav9"],
            name="Grand Opening Announcement",
            segments=["seg_01jxwtwzqhfykb31dt6mvpsa9k"],
            send_at=parse_datetime("2024-02-01T15:00:00Z"),
            to=["seg_01j9dy8mdzfn3r0e8x1tbdrdrf", "ctc_01j9dy8mdzfn3r0e8x1tbdrdrf", "+18015551234", "+18015555678"],
        )
        assert_matches_type(AccountBlastsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_blasts(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.blasts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountBlastsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_blasts(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.blasts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountBlastsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_blasts(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.blasts(
                account_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_campaigns(self, client: Surge) -> None:
        account = client.accounts.campaigns(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
            description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
            message_samples=[
                "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
            ],
            privacy_policy_url="https://fastauto.shop/sms-privacy",
            use_cases=["account_notification", "customer_care", "marketing"],
            volume="high",
        )
        assert_matches_type(AccountCampaignsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_campaigns_with_all_params(self, client: Surge) -> None:
        account = client.accounts.campaigns(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
            description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
            message_samples=[
                "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
            ],
            privacy_policy_url="https://fastauto.shop/sms-privacy",
            use_cases=["account_notification", "customer_care", "marketing"],
            volume="high",
            includes=["links", "phone_numbers"],
            link_sample="https://l.fastauto.shop/s034ij",
            terms_and_conditions_url="https://fastauto.shop/terms-and-conditions",
        )
        assert_matches_type(AccountCampaignsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_campaigns(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.campaigns(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
            description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
            message_samples=[
                "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
            ],
            privacy_policy_url="https://fastauto.shop/sms-privacy",
            use_cases=["account_notification", "customer_care", "marketing"],
            volume="high",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCampaignsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_campaigns(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.campaigns(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
            description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
            message_samples=[
                "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
            ],
            privacy_policy_url="https://fastauto.shop/sms-privacy",
            use_cases=["account_notification", "customer_care", "marketing"],
            volume="high",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountCampaignsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_campaigns(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.campaigns(
                account_id="",
                consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
                description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
                message_samples=[
                    "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                    "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                    "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
                ],
                privacy_policy_url="https://fastauto.shop/sms-privacy",
                use_cases=["account_notification", "customer_care", "marketing"],
                volume="high",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_contacts(self, client: Surge) -> None:
        account = client.accounts.contacts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            phone_number="+18015551234",
        )
        assert_matches_type(AccountContactsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_contacts_with_all_params(self, client: Surge) -> None:
        account = client.accounts.contacts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            phone_number="+18015551234",
            email="dom@toretto.family",
            first_name="Dominic",
            last_name="Toretto",
            metadata={"car": "1970 Dodge Charger R/T"},
        )
        assert_matches_type(AccountContactsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_contacts(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.contacts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            phone_number="+18015551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountContactsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_contacts(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.contacts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            phone_number="+18015551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountContactsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_contacts(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.contacts(
                account_id="",
                phone_number="+18015551234",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_messages_overload_1(self, client: Surge) -> None:
        account = client.accounts.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={"contact": {"phone_number": "+18015551234"}},
        )
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_messages_with_all_params_overload_1(self, client: Surge) -> None:
        account = client.accounts.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={
                "contact": {
                    "phone_number": "+18015551234",
                    "email": "dev@stainless.com",
                    "first_name": "Dominic",
                    "last_name": "Toretto",
                    "metadata": {"foo": "string"},
                },
                "phone_number": "+18015556789",
            },
            attachments=[{"url": "https://toretto.family/coronas.gif"}],
            body="body",
            send_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_messages_overload_1(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={"contact": {"phone_number": "+18015551234"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_messages_overload_1(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={"contact": {"phone_number": "+18015551234"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountMessagesResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_messages_overload_1(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.messages(
                account_id="",
                conversation={"contact": {"phone_number": "+18015551234"}},
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_messages_overload_2(self, client: Surge) -> None:
        account = client.accounts.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            to="+18015551234",
        )
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_messages_with_all_params_overload_2(self, client: Surge) -> None:
        account = client.accounts.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            to="+18015551234",
            attachments=[{"url": "https://toretto.family/coronas.gif"}],
            body="body",
            from_="+18015552345",
            send_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_messages_overload_2(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            to="+18015551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_messages_overload_2(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            to="+18015551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountMessagesResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_messages_overload_2(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.messages(
                account_id="",
                to="+18015551234",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_phone_numbers(self, client: Surge) -> None:
        account = client.accounts.phone_numbers(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            type="local",
        )
        assert_matches_type(AccountPhoneNumbersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_phone_numbers_with_all_params(self, client: Surge) -> None:
        account = client.accounts.phone_numbers(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            type="local",
            area_code="801",
        )
        assert_matches_type(AccountPhoneNumbersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_phone_numbers(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.phone_numbers(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            type="local",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountPhoneNumbersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_phone_numbers(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.phone_numbers(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            type="local",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountPhoneNumbersResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_phone_numbers(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.phone_numbers(
                account_id="",
                type="local",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_retrieve_status(self, client: Surge) -> None:
        account = client.accounts.retrieve_status(
            account_id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        )
        assert_matches_type(AccountRetrieveStatusResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_retrieve_status_with_all_params(self, client: Surge) -> None:
        account = client.accounts.retrieve_status(
            account_id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
            capabilities=["local_messaging"],
        )
        assert_matches_type(AccountRetrieveStatusResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_retrieve_status(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.retrieve_status(
            account_id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveStatusResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.retrieve_status(
            account_id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveStatusResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_retrieve_status(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve_status(
                account_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_users(self, client: Surge) -> None:
        account = client.accounts.users(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            first_name="Brian",
        )
        assert_matches_type(AccountUsersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_users_with_all_params(self, client: Surge) -> None:
        account = client.accounts.users(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            first_name="Brian",
            last_name="O'Conner",
            metadata={
                "email": "boconner@toretti.family",
                "user_id": "string",
            },
            photo_url="https://toretti.family/people/brian.jpg",
        )
        assert_matches_type(AccountUsersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_users(self, client: Surge) -> None:
        response = client.accounts.with_raw_response.users(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            first_name="Brian",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUsersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_users(self, client: Surge) -> None:
        with client.accounts.with_streaming_response.users(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            first_name="Brian",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountUsersResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_users(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.users(
                account_id="",
                first_name="Brian",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.create(
            name="Account #2840 - DT Precision Auto",
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.create(
            name="Account #2840 - DT Precision Auto",
            brand_name="DT Precision Auto",
            organization={
                "address": {
                    "country": "US",
                    "line1": "2640 Huron St",
                    "line2": None,
                    "locality": "Los Angeles",
                    "name": "DT Precision Auto",
                    "postal_code": "90065",
                    "region": "CA",
                },
                "contact": {
                    "email": "dom@dtprecisionauto.com",
                    "first_name": "Dominic",
                    "last_name": "Toretto",
                    "phone_number": "+13235556439",
                    "title": "other",
                    "title_other": "Owner",
                },
                "country": "US",
                "email": "dom@dtprecisionauto.com",
                "identifier": "123456789",
                "identifier_type": "ein",
                "industry": "automotive",
                "mobile_number": "+13235556439",
                "regions_of_operation": ["usa_and_canada"],
                "registered_name": "DT Precision Auto LLC",
                "stock_exchange": None,
                "stock_symbol": None,
                "type": "llc",
                "website": "https://dtprecisionauto.com",
            },
            time_zone="America/Los_Angeles",
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.create(
            name="Account #2840 - DT Precision Auto",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.create(
            name="Account #2840 - DT Precision Auto",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_update(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.update(
            id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.update(
            id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
            brand_name="DT Precision Auto",
            name="D·T Precision Auto Shop",
            organization={
                "address": {
                    "country": "US",
                    "line1": "2640 Huron St",
                    "line2": None,
                    "locality": "Los Angeles",
                    "name": "DT Precision Auto",
                    "postal_code": "90065",
                    "region": "CA",
                },
                "contact": {
                    "email": "dom@dtprecisionauto.com",
                    "first_name": "Dominic",
                    "last_name": "Toretto",
                    "phone_number": "+13235556439",
                    "title": "other",
                    "title_other": "Owner",
                },
                "country": "US",
                "email": "dom@dtprecisionauto.com",
                "identifier": "123456789",
                "identifier_type": "ein",
                "industry": "automotive",
                "mobile_number": "+13235556439",
                "regions_of_operation": ["usa_and_canada"],
                "registered_name": "DT Precision Auto LLC",
                "stock_exchange": None,
                "stock_symbol": None,
                "type": "llc",
                "website": "https://dtprecisionauto.com",
            },
            time_zone="America/Los_Angeles",
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.update(
            id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.update(
            id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_blasts(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.blasts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(AccountBlastsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_blasts_with_all_params(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.blasts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            attachments=[{"url": "https://example.com/image.jpg"}],
            body="Join us for our grand opening!",
            contacts=["ctc_01jxwtp1vse91twb5bj977gav9"],
            name="Grand Opening Announcement",
            segments=["seg_01jxwtwzqhfykb31dt6mvpsa9k"],
            send_at=parse_datetime("2024-02-01T15:00:00Z"),
            to=["seg_01j9dy8mdzfn3r0e8x1tbdrdrf", "ctc_01j9dy8mdzfn3r0e8x1tbdrdrf", "+18015551234", "+18015555678"],
        )
        assert_matches_type(AccountBlastsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_blasts(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.blasts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountBlastsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_blasts(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.blasts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountBlastsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_blasts(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.blasts(
                account_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_campaigns(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.campaigns(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
            description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
            message_samples=[
                "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
            ],
            privacy_policy_url="https://fastauto.shop/sms-privacy",
            use_cases=["account_notification", "customer_care", "marketing"],
            volume="high",
        )
        assert_matches_type(AccountCampaignsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_campaigns_with_all_params(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.campaigns(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
            description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
            message_samples=[
                "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
            ],
            privacy_policy_url="https://fastauto.shop/sms-privacy",
            use_cases=["account_notification", "customer_care", "marketing"],
            volume="high",
            includes=["links", "phone_numbers"],
            link_sample="https://l.fastauto.shop/s034ij",
            terms_and_conditions_url="https://fastauto.shop/terms-and-conditions",
        )
        assert_matches_type(AccountCampaignsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_campaigns(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.campaigns(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
            description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
            message_samples=[
                "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
            ],
            privacy_policy_url="https://fastauto.shop/sms-privacy",
            use_cases=["account_notification", "customer_care", "marketing"],
            volume="high",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountCampaignsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_campaigns(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.campaigns(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
            description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
            message_samples=[
                "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
            ],
            privacy_policy_url="https://fastauto.shop/sms-privacy",
            use_cases=["account_notification", "customer_care", "marketing"],
            volume="high",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountCampaignsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_campaigns(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.campaigns(
                account_id="",
                consent_flow="When customers bring in their car for service, they will fill out this web form for intake: https://fastauto.shop/bp108c In it they can choose to opt in to text message notifications. If they choose to opt in, we will send them notifications to let them know if our mechanics find issues and once the car is ready to go, as well as links to invoices and to leave us feedback.",
                description="This phone number will send auto maintenance notifications to end users that have opted in. It will also be used for responding to customer inquiries and sending some marketing offers.",
                message_samples=[
                    "You are now opted in to receive repair notifications from DT Precision Auto. Frequency varies. Msg&data rates apply. Reply STOP to opt out.",
                    "You're lucky that hundred shot of NOS didn't blow the welds on the intake!",
                    "Your car is ready to go. See your invoice here: https://l.fastauto.shop/s034ij",
                ],
                privacy_policy_url="https://fastauto.shop/sms-privacy",
                use_cases=["account_notification", "customer_care", "marketing"],
                volume="high",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_contacts(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.contacts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            phone_number="+18015551234",
        )
        assert_matches_type(AccountContactsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_contacts_with_all_params(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.contacts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            phone_number="+18015551234",
            email="dom@toretto.family",
            first_name="Dominic",
            last_name="Toretto",
            metadata={"car": "1970 Dodge Charger R/T"},
        )
        assert_matches_type(AccountContactsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_contacts(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.contacts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            phone_number="+18015551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountContactsResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_contacts(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.contacts(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            phone_number="+18015551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountContactsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_contacts(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.contacts(
                account_id="",
                phone_number="+18015551234",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_messages_overload_1(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={"contact": {"phone_number": "+18015551234"}},
        )
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_messages_with_all_params_overload_1(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={
                "contact": {
                    "phone_number": "+18015551234",
                    "email": "dev@stainless.com",
                    "first_name": "Dominic",
                    "last_name": "Toretto",
                    "metadata": {"foo": "string"},
                },
                "phone_number": "+18015556789",
            },
            attachments=[{"url": "https://toretto.family/coronas.gif"}],
            body="body",
            send_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_messages_overload_1(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={"contact": {"phone_number": "+18015551234"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_messages_overload_1(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={"contact": {"phone_number": "+18015551234"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountMessagesResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_messages_overload_1(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.messages(
                account_id="",
                conversation={"contact": {"phone_number": "+18015551234"}},
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_messages_overload_2(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            to="+18015551234",
        )
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_messages_with_all_params_overload_2(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            to="+18015551234",
            attachments=[{"url": "https://toretto.family/coronas.gif"}],
            body="body",
            from_="+18015552345",
            send_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_messages_overload_2(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            to="+18015551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountMessagesResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_messages_overload_2(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.messages(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            to="+18015551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountMessagesResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_messages_overload_2(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.messages(
                account_id="",
                to="+18015551234",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_phone_numbers(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.phone_numbers(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            type="local",
        )
        assert_matches_type(AccountPhoneNumbersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_phone_numbers_with_all_params(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.phone_numbers(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            type="local",
            area_code="801",
        )
        assert_matches_type(AccountPhoneNumbersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_phone_numbers(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.phone_numbers(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            type="local",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountPhoneNumbersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_phone_numbers(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.phone_numbers(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            type="local",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountPhoneNumbersResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_phone_numbers(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.phone_numbers(
                account_id="",
                type="local",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.retrieve_status(
            account_id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        )
        assert_matches_type(AccountRetrieveStatusResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_retrieve_status_with_all_params(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.retrieve_status(
            account_id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
            capabilities=["local_messaging"],
        )
        assert_matches_type(AccountRetrieveStatusResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.retrieve_status(
            account_id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveStatusResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.retrieve_status(
            account_id="acct_01jpqjvfg9enpt7pyxd60pcmxj",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveStatusResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve_status(
                account_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_users(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.users(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            first_name="Brian",
        )
        assert_matches_type(AccountUsersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_users_with_all_params(self, async_client: AsyncSurge) -> None:
        account = await async_client.accounts.users(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            first_name="Brian",
            last_name="O'Conner",
            metadata={
                "email": "boconner@toretti.family",
                "user_id": "string",
            },
            photo_url="https://toretti.family/people/brian.jpg",
        )
        assert_matches_type(AccountUsersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_users(self, async_client: AsyncSurge) -> None:
        response = await async_client.accounts.with_raw_response.users(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            first_name="Brian",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountUsersResponse, account, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_users(self, async_client: AsyncSurge) -> None:
        async with async_client.accounts.with_streaming_response.users(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            first_name="Brian",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountUsersResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_users(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.users(
                account_id="",
                first_name="Brian",
            )
