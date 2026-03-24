# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from surge import Surge, AsyncSurge
from surge.types import (
    RecordingListResponse,
    RecordingDeleteResponse,
    RecordingGetFileResponse,
    RecordingRetrieveResponse,
)
from tests.utils import assert_matches_type
from surge.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecordings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Surge) -> None:
        recording = client.recordings.retrieve(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Surge) -> None:
        response = client.recordings.with_raw_response.retrieve(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Surge) -> None:
        with client.recordings.with_streaming_response.retrieve(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.recordings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Surge) -> None:
        recording = client.recordings.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(SyncCursor[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Surge) -> None:
        recording = client.recordings.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            after="after",
            before="before",
        )
        assert_matches_type(SyncCursor[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Surge) -> None:
        response = client.recordings.with_raw_response.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(SyncCursor[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Surge) -> None:
        with client.recordings.with_streaming_response.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(SyncCursor[RecordingListResponse], recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.recordings.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Surge) -> None:
        recording = client.recordings.delete(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Surge) -> None:
        response = client.recordings.with_raw_response.delete(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Surge) -> None:
        with client.recordings.with_streaming_response.delete(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Surge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.recordings.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_file(self, client: Surge) -> None:
        recording = client.recordings.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_file(self, client: Surge) -> None:
        response = client.recordings.with_raw_response.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSurge) -> None:
        recording = await async_client.recordings.retrieve(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSurge) -> None:
        response = await async_client.recordings.with_raw_response.retrieve(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSurge) -> None:
        async with async_client.recordings.with_streaming_response.retrieve(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.recordings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSurge) -> None:
        recording = await async_client.recordings.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )
        assert_matches_type(AsyncCursor[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSurge) -> None:
        recording = await async_client.recordings.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
            after="after",
            before="before",
        )
        assert_matches_type(AsyncCursor[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSurge) -> None:
        response = await async_client.recordings.with_raw_response.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(AsyncCursor[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSurge) -> None:
        async with async_client.recordings.with_streaming_response.list(
            account_id="acct_01j9a43avnfqzbjfch6pygv1td",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(AsyncCursor[RecordingListResponse], recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.recordings.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSurge) -> None:
        recording = await async_client.recordings.delete(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSurge) -> None:
        response = await async_client.recordings.with_raw_response.delete(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSurge) -> None:
        async with async_client.recordings.with_streaming_response.delete(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.recordings.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_file(self, async_client: AsyncSurge) -> None:
        recording = await async_client.recordings.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )
        assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_file(self, async_client: AsyncSurge) -> None:
        response = await async_client.recordings.with_raw_response.get_file(
            "rec_01kfyc9dgdec1avkgs7tng8htg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingGetFileResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_file(self, async_client: AsyncSurge) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.recordings.with_raw_response.get_file(
                "",
            )
