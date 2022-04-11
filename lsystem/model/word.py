from __future__ import annotations
from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from lsystem.model.alphabet import Alphabet

import lsystem.model.symbol as symbol


class Word():

    def __init__(self, symbols: Union[str, List[symbol.Symbol]]) -> None:

        if isinstance(symbols, str):
            self.symbols = [symbol.Symbol(x) for x in symbols]

        elif all(map(lambda x: isinstance(x, symbol.Symbol), symbols)):
            self.symbols = symbols

        else:
            raise TypeError(
                'Invalid type. Word must consist of a List[Symbol] or a str')

    def in_alphabet(self, alphabet: Alphabet) -> bool:
        return all(map(lambda x: x in alphabet, self.symbols))

    def __repr__(self) -> str:
        return f'<{self.__module__}.Word, {hex(id(self))}>'

    def __str__(self) -> str:
        return ''.join(map(str, self.symbols))

    def __eq__(self, __x: object) -> bool:
        if (not isinstance(__x, self.__class__)
                or not len(__x.symbols) == len(self.symbols)):
            return False

        return all(map(lambda x: x[0] == x[1], zip(__x.symbols, self.symbols)))

    def __hash__(self) -> int:
        return hash(self.__str__())

    def append(self, other: Union[symbol.Symbol, Word]) -> None:
        if isinstance(other, symbol.Symbol):
            self.symbols.append(other)
        elif isinstance(other, Word):
            self.symbols.extend(other.symbols)
        else:
            raise TypeError(
                'Invalid type for Word.append() method, requires a Word or Symbol argument.')

    def extend(self, w: Word) -> None:

        if not isinstance(w, Word):
            raise TypeError(f'Argument {type(w)} is not of type Word.')

        self.symbols.extend(w.symbols)
