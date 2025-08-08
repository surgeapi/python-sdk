# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from surgeapi import Surge, AsyncSurge
from tests.utils import assert_matches_type
from surgeapi.types import MessageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create(self, client: Surge) -> None:
        message = client.messages.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={},
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create_with_all_params(self, client: Surge) -> None:
        message = client.messages.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={
                "id": "cnv_01j9e0dgmdfkj86c877ws0znae",
                "contact": {
                    "id": "ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
                    "first_name": "Dominic",
                    "last_name": "Toretto",
                    "phone_number": "+18015551234",
                },
            },
            attachments=[{"url": "https://toretto.family/coronas.gif"}],
            body="Thought you could leave without saying goodbye?",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_create(self, client: Surge) -> None:
        response = client.messages.with_raw_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_create(self, client: Surge) -> None:
        with client.messages.with_streaming_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_create(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.messages.with_raw_response.create(
                account_id="",
                conversation={},
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncSurge) -> None:
        message = await async_client.messages.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={},
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSurge) -> None:
        message = await async_client.messages.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={
                "id": "cnv_01j9e0dgmdfkj86c877ws0znae",
                "contact": {
                    "id": "ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
                    "first_name": "Dominic",
                    "last_name": "Toretto",
                    "phone_number": "+18015551234",
                },
            },
            attachments=[{"url": "https://toretto.family/coronas.gif"}],
            body="Thought you could leave without saying goodbye?",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSurge) -> None:
        response = await async_client.messages.with_raw_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSurge) -> None:
        async with async_client.messages.with_streaming_response.create(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            conversation={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_create(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.messages.with_raw_response.create(
                account_id="",
                conversation={},
            )
