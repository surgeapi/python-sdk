# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from surge import Surge, AsyncSurge
from surge.types import AttachmentGetFileResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_file(self, client: Surge) -> None:
        attachment = client.attachments.get_file(
            "att_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(AttachmentGetFileResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_file(self, client: Surge) -> None:
        response = client.attachments.with_raw_response.get_file(
            "att_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentGetFileResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_file(self, client: Surge) -> None:
        with client.attachments.with_streaming_response.get_file(
            "att_01kfyc9dgdec1avkgs7tng8htg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentGetFileResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_file(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            client.attachments.with_raw_response.get_file(
                "",
            )


class TestAsyncAttachments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_file(self, async_client: AsyncSurge) -> None:
        attachment = await async_client.attachments.get_file(
            "att_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(AttachmentGetFileResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_file(self, async_client: AsyncSurge) -> None:
        response = await async_client.attachments.with_raw_response.get_file(
            "att_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentGetFileResponse, attachment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_file(self, async_client: AsyncSurge) -> None:
        async with async_client.attachments.with_streaming_response.get_file(
            "att_01kfyc9dgdec1avkgs7tng8htg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentGetFileResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_file(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            await async_client.attachments.with_raw_response.get_file(
                "",
            )
