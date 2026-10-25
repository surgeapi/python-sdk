# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from surge import Surge, AsyncSurge
from surge.types import (
    TollFreeCampaign,
)
from tests.utils import assert_matches_type
from surge.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTollFreeCampaigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Surge) -> None:
        toll_free_campaign = client.toll_free_campaigns.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            message_samples=["string"],
            phone_number_id="phone_number_id",
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Surge) -> None:
        toll_free_campaign = client.toll_free_campaigns.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            message_samples=["string"],
            phone_number_id="phone_number_id",
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
            includes=["age_gated"],
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Surge) -> None:
        response = client.toll_free_campaigns.with_raw_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            message_samples=["string"],
            phone_number_id="phone_number_id",
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toll_free_campaign = response.parse()
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Surge) -> None:
        with client.toll_free_campaigns.with_streaming_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            message_samples=["string"],
            phone_number_id="phone_number_id",
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toll_free_campaign = response.parse()
            assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.toll_free_campaigns.with_raw_response.create(
                account_id="",
                consent_flows=[
                    {
                        "script": "xxxxxxxxxxxxxxxxxxxx",
                        "type": "verbal",
                    }
                ],
                description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                message_samples=["string"],
                phone_number_id="phone_number_id",
                privacy_policy_url="https://example.com",
                terms_and_conditions_url="https://example.com",
                use_cases=["two_factor_authentication"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Surge) -> None:
        toll_free_campaign = client.toll_free_campaigns.retrieve(
            "tfc_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Surge) -> None:
        response = client.toll_free_campaigns.with_raw_response.retrieve(
            "tfc_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toll_free_campaign = response.parse()
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Surge) -> None:
        with client.toll_free_campaigns.with_streaming_response.retrieve(
            "tfc_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toll_free_campaign = response.parse()
            assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.toll_free_campaigns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Surge) -> None:
        toll_free_campaign = client.toll_free_campaigns.update(
            campaign_id="tfc_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Surge) -> None:
        toll_free_campaign = client.toll_free_campaigns.update(
            campaign_id="tfc_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            includes=["age_gated"],
            message_samples=["string"],
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Surge) -> None:
        response = client.toll_free_campaigns.with_raw_response.update(
            campaign_id="tfc_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toll_free_campaign = response.parse()
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Surge) -> None:
        with client.toll_free_campaigns.with_streaming_response.update(
            campaign_id="tfc_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toll_free_campaign = response.parse()
            assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.toll_free_campaigns.with_raw_response.update(
                campaign_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Surge) -> None:
        toll_free_campaign = client.toll_free_campaigns.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(SyncCursor[TollFreeCampaign], toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Surge) -> None:
        toll_free_campaign = client.toll_free_campaigns.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            after="after",
            before="before",
        )
        assert_matches_type(SyncCursor[TollFreeCampaign], toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Surge) -> None:
        response = client.toll_free_campaigns.with_raw_response.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toll_free_campaign = response.parse()
        assert_matches_type(SyncCursor[TollFreeCampaign], toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Surge) -> None:
        with client.toll_free_campaigns.with_streaming_response.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toll_free_campaign = response.parse()
            assert_matches_type(SyncCursor[TollFreeCampaign], toll_free_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.toll_free_campaigns.with_raw_response.list(
                account_id="",
            )


class TestAsyncTollFreeCampaigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSurge) -> None:
        toll_free_campaign = await async_client.toll_free_campaigns.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            message_samples=["string"],
            phone_number_id="phone_number_id",
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSurge) -> None:
        toll_free_campaign = await async_client.toll_free_campaigns.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            message_samples=["string"],
            phone_number_id="phone_number_id",
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
            includes=["age_gated"],
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSurge) -> None:
        response = await async_client.toll_free_campaigns.with_raw_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            message_samples=["string"],
            phone_number_id="phone_number_id",
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toll_free_campaign = await response.parse()
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSurge) -> None:
        async with async_client.toll_free_campaigns.with_streaming_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            message_samples=["string"],
            phone_number_id="phone_number_id",
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toll_free_campaign = await response.parse()
            assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.toll_free_campaigns.with_raw_response.create(
                account_id="",
                consent_flows=[
                    {
                        "script": "xxxxxxxxxxxxxxxxxxxx",
                        "type": "verbal",
                    }
                ],
                description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                message_samples=["string"],
                phone_number_id="phone_number_id",
                privacy_policy_url="https://example.com",
                terms_and_conditions_url="https://example.com",
                use_cases=["two_factor_authentication"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSurge) -> None:
        toll_free_campaign = await async_client.toll_free_campaigns.retrieve(
            "tfc_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSurge) -> None:
        response = await async_client.toll_free_campaigns.with_raw_response.retrieve(
            "tfc_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toll_free_campaign = await response.parse()
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSurge) -> None:
        async with async_client.toll_free_campaigns.with_streaming_response.retrieve(
            "tfc_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toll_free_campaign = await response.parse()
            assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.toll_free_campaigns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSurge) -> None:
        toll_free_campaign = await async_client.toll_free_campaigns.update(
            campaign_id="tfc_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSurge) -> None:
        toll_free_campaign = await async_client.toll_free_campaigns.update(
            campaign_id="tfc_01j9a43avnfqzbjfch6pygv1td",
            consent_flows=[
                {
                    "script": "xxxxxxxxxxxxxxxxxxxx",
                    "type": "verbal",
                }
            ],
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            includes=["age_gated"],
            message_samples=["string"],
            privacy_policy_url="https://example.com",
            terms_and_conditions_url="https://example.com",
            use_cases=["two_factor_authentication"],
        )
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSurge) -> None:
        response = await async_client.toll_free_campaigns.with_raw_response.update(
            campaign_id="tfc_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toll_free_campaign = await response.parse()
        assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSurge) -> None:
        async with async_client.toll_free_campaigns.with_streaming_response.update(
            campaign_id="tfc_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toll_free_campaign = await response.parse()
            assert_matches_type(TollFreeCampaign, toll_free_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.toll_free_campaigns.with_raw_response.update(
                campaign_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSurge) -> None:
        toll_free_campaign = await async_client.toll_free_campaigns.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(AsyncCursor[TollFreeCampaign], toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSurge) -> None:
        toll_free_campaign = await async_client.toll_free_campaigns.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            after="after",
            before="before",
        )
        assert_matches_type(AsyncCursor[TollFreeCampaign], toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSurge) -> None:
        response = await async_client.toll_free_campaigns.with_raw_response.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toll_free_campaign = await response.parse()
        assert_matches_type(AsyncCursor[TollFreeCampaign], toll_free_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSurge) -> None:
        async with async_client.toll_free_campaigns.with_streaming_response.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toll_free_campaign = await response.parse()
            assert_matches_type(AsyncCursor[TollFreeCampaign], toll_free_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.toll_free_campaigns.with_raw_response.list(
                account_id="",
            )
