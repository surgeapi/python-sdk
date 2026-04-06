# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from surge import Surge, AsyncSurge
from surge.types import (
    Contact,
    AudienceCreateResponse,
)
from tests.utils import assert_matches_type
from surge.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Surge) -> None:
        audience = client.audiences.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            name="The Family",
        )
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Surge) -> None:
        response = client.audiences.with_raw_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            name="The Family",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Surge) -> None:
        with client.audiences.with_streaming_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            name="The Family",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceCreateResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.audiences.with_raw_response.create(
                account_id="",
                name="The Family",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_contact(self, client: Surge) -> None:
        audience = client.audiences.add_contact(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
            id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
        )
        assert_matches_type(Contact, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_contact(self, client: Surge) -> None:
        response = client.audiences.with_raw_response.add_contact(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
            id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(Contact, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_contact(self, client: Surge) -> None:
        with client.audiences.with_streaming_response.add_contact(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
            id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(Contact, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_contact(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.add_contact(
                audience_id="",
                id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_contacts(self, client: Surge) -> None:
        audience = client.audiences.list_contacts(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(SyncCursor[Contact], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_contacts_with_all_params(self, client: Surge) -> None:
        audience = client.audiences.list_contacts(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
            after="after",
            before="before",
        )
        assert_matches_type(SyncCursor[Contact], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_contacts(self, client: Surge) -> None:
        response = client.audiences.with_raw_response.list_contacts(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(SyncCursor[Contact], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_contacts(self, client: Surge) -> None:
        with client.audiences.with_streaming_response.list_contacts(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(SyncCursor[Contact], audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_contacts(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.list_contacts(
                audience_id="",
            )


class TestAsyncAudiences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSurge) -> None:
        audience = await async_client.audiences.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            name="The Family",
        )
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSurge) -> None:
        response = await async_client.audiences.with_raw_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            name="The Family",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceCreateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSurge) -> None:
        async with async_client.audiences.with_streaming_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            name="The Family",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceCreateResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.audiences.with_raw_response.create(
                account_id="",
                name="The Family",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_contact(self, async_client: AsyncSurge) -> None:
        audience = await async_client.audiences.add_contact(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
            id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
        )
        assert_matches_type(Contact, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_contact(self, async_client: AsyncSurge) -> None:
        response = await async_client.audiences.with_raw_response.add_contact(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
            id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(Contact, audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_contact(self, async_client: AsyncSurge) -> None:
        async with async_client.audiences.with_streaming_response.add_contact(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
            id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(Contact, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_contact(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.add_contact(
                audience_id="",
                id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_contacts(self, async_client: AsyncSurge) -> None:
        audience = await async_client.audiences.list_contacts(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(AsyncCursor[Contact], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_contacts_with_all_params(self, async_client: AsyncSurge) -> None:
        audience = await async_client.audiences.list_contacts(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
            after="after",
            before="before",
        )
        assert_matches_type(AsyncCursor[Contact], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_contacts(self, async_client: AsyncSurge) -> None:
        response = await async_client.audiences.with_raw_response.list_contacts(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AsyncCursor[Contact], audience, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_contacts(self, async_client: AsyncSurge) -> None:
        async with async_client.audiences.with_streaming_response.list_contacts(
            audience_id="aud_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AsyncCursor[Contact], audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_contacts(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.list_contacts(
                audience_id="",
            )
