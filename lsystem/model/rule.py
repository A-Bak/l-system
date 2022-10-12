from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lsystem.model.word import Word

from lsystem.model.symbol import Symbol

__all__ = ["Rule"]


class Rule:
    def __init__(self, left_side: Symbol, right_side: Word) -> None:
        super().__init__()

        if not (isinstance(left_side, Symbol) or isinstance(right_side, Word)):
            raise TypeError(
                "Left and right sight of a rule must consist of Symbol (NonTerminal/Terminal) characters."
            )

        self.left_side = left_side
        self.right_side = right_side

    def is_applicable(self, s: Symbol) -> bool:
        if not isinstance(s, Symbol):
            raise TypeError("Symbol is ")

        return self.left_side == s

    def __repr__(self) -> str:
        return f"<{self.__module__}.Rule, {hex(id(self))}>"

    def __str__(self) -> str:
        return f"{self.left_side} -> {str(self.right_side)}"

    def __eq__(self, __x: object) -> bool:
        return (
            self.left_side == __x.left_side and self.right_side == __x.right_side
            if isinstance(__x, Rule)
            else False
        )

    def __hash__(self) -> int:
        return hash((self.left_side, self.right_side))
