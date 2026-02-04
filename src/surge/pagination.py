# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["CursorPagination", "SyncCursor", "AsyncCursor"]

_T = TypeVar("_T")


class CursorPagination(BaseModel):
    next_cursor: Optional[str] = None

    previous_cursor: Optional[str] = None


class SyncCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[CursorPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        if self._options.params.get("before"):
            previous_cursor = None
            if self.pagination is not None:
                if self.pagination.previous_cursor is not None:
                    previous_cursor = self.pagination.previous_cursor
            if not previous_cursor:
                return None

            return PageInfo(params={"before": previous_cursor})

        next_cursor = None
        if self.pagination is not None:
            if self.pagination.next_cursor is not None:
                next_cursor = self.pagination.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"after": next_cursor})


class AsyncCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[CursorPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        if self._options.params.get("before"):
            previous_cursor = None
            if self.pagination is not None:
                if self.pagination.previous_cursor is not None:
                    previous_cursor = self.pagination.previous_cursor
            if not previous_cursor:
                return None

            return PageInfo(params={"before": previous_cursor})

        next_cursor = None
        if self.pagination is not None:
            if self.pagination.next_cursor is not None:
                next_cursor = self.pagination.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"after": next_cursor})
