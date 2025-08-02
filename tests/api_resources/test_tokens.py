# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from surgeapi import Surge, AsyncSurge
from tests.utils import assert_matches_type
from surgeapi.types import TokenCreateTokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create_token(self, client: Surge) -> None:
        token = client.tokens.create_token(
            user_id="usr_01jymgdfrpec2asc5m0z3a6fr9",
        )
        assert_matches_type(TokenCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create_token_with_all_params(self, client: Surge) -> None:
        token = client.tokens.create_token(
            user_id="usr_01jymgdfrpec2asc5m0z3a6fr9",
            duration_seconds=900,
        )
        assert_matches_type(TokenCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_create_token(self, client: Surge) -> None:
        response = client.tokens.with_raw_response.create_token(
            user_id="usr_01jymgdfrpec2asc5m0z3a6fr9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_create_token(self, client: Surge) -> None:
        with client.tokens.with_streaming_response.create_token(
            user_id="usr_01jymgdfrpec2asc5m0z3a6fr9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenCreateTokenResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_create_token(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.tokens.with_raw_response.create_token(
                user_id="",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create_token(self, async_client: AsyncSurge) -> None:
        token = await async_client.tokens.create_token(
            user_id="usr_01jymgdfrpec2asc5m0z3a6fr9",
        )
        assert_matches_type(TokenCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create_token_with_all_params(self, async_client: AsyncSurge) -> None:
        token = await async_client.tokens.create_token(
            user_id="usr_01jymgdfrpec2asc5m0z3a6fr9",
            duration_seconds=900,
        )
        assert_matches_type(TokenCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_create_token(self, async_client: AsyncSurge) -> None:
        response = await async_client.tokens.with_raw_response.create_token(
            user_id="usr_01jymgdfrpec2asc5m0z3a6fr9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_create_token(self, async_client: AsyncSurge) -> None:
        async with async_client.tokens.with_streaming_response.create_token(
            user_id="usr_01jymgdfrpec2asc5m0z3a6fr9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenCreateTokenResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_create_token(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.tokens.with_raw_response.create_token(
                user_id="",
            )
