"""sqlite3 SQL builder"""
from __future__ import annotations

import abc
import typing
if typing.TYPE_CHECKING:
    import sqlite3

class SqlStatement(abc.ABC):
    __slots__ = ('parts', )

    def __init__(self, items: list[str]):
        self.parts: list[str] = items

    def export_str(self) -> str:
        return ''.join(self.parts)

    def execute(self, cur: sqlite3.Cursor, params=()):
        cur.execute(self.export_str(), params)
        return cur


class Select(SqlStatement):
    def __init__(self, init: str):
        super().__init__([init])

    def where(self, cond: str) -> typing.Self:
        self.parts.append(' WHERE ')
        self.parts.append(cond)
        return self

    def order_by(self, cols: str, desc=False) -> typing.Self:
        self.parts.append(' ORDER BY ')
        self.parts.append(cols)
        self.parts.append(' DESC ' if desc else ' ASC ')
        return self
