# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from surge import Surge, AsyncSurge
from surge.types import RecordingGetFileResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecordings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_get_file(self, client: Surge) -> None:
        recording = client.recordings.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_raw_response_get_file(self, client: Surge) -> None:
        response = client.recordings.with_raw_response.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_streaming_response_get_file(self, client: Surge) -> None:
        with client.recordings.with_streaming_response.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_path_params_get_file(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.recordings.with_raw_response.get_file(
                "",
            )


class TestAsyncRecordings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_get_file(self, async_client: AsyncSurge) -> None:
        recording = await async_client.recordings.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_raw_response_get_file(self, async_client: AsyncSurge) -> None:
        response = await async_client.recordings.with_raw_response.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_streaming_response_get_file(self, async_client: AsyncSurge) -> None:
        async with async_client.recordings.with_streaming_response.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_path_params_get_file(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.recordings.with_raw_response.get_file(
                "",
            )
