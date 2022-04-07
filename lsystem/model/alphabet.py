from __future__ import annotations
from typing import List

import lsystem.model.symbol as symbol


__all__ = ['Alphabet']


class Alphabet:

    def __init__(self, nonterminals: List[symbol.Symbol], terminals: List[symbol.Symbol]) -> None:

        def is_symbol(x): return isinstance(x, symbol.Symbol)

        if not all(map(is_symbol, nonterminals)) or not all(map(is_symbol, terminals)):
            raise TypeError(
                'Alphabet nonterminals and terminals must be of class ')

        self.nonterminals = set(nonterminals)
        self.terminals = set(terminals)

        self.characters = self.nonterminals.union(self.terminals)

    def add_nonterminal(self, s: symbol.Symbol) -> None:
        self.nonterminals.add(s)

    def add_terminal(self, s: symbol.Symbol) -> None:
        self.terminals.add(s)

    def is_nonterminal(self, key: symbol.Symbol) -> bool:
        return key in self.nonterminals

    def is_terminal(self, key: symbol.Symbol) -> bool:
        return key in self.terminals

    def __or__(self, other: object) -> Alphabet:
        return self.union(other)

    def union(self, other: Alphabet) -> Alphabet:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f'Invalid operand {other}. Union needs two operands of type {self.__module__}.Alphabet')

        nt = self.nonterminals.union(other.nonterminals)
        t = self.terminals.union(other.terminals)
        return Alphabet(nt, t)

    def __sub__(self, other: object) -> Alphabet:
        return self.difference(other)

    def difference(self, other: object) -> Alphabet:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f'Invalid operand {other}. Difference needs two operands of type {self.__module__}.Alphabet')

        nt = self.nonterminals.difference(other.nonterminals)
        t = self.terminals.difference(other.terminals)
        return Alphabet(nt, t)

    def __and__(self, other: object) -> Alphabet:
        return self.intersection(other)

    def intersection(self, other: object) -> Alphabet:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f'Invalid operand {other}. Intersection needs two operands of type {self.__module__}.Alphabet')

        nt = self.nonterminals.intersection(other.nonterminals)
        t = self.terminals.intersection(other.terminals)
        return Alphabet(nt, t)

    def __contains__(self, key: symbol.Symbol) -> bool:
        return key in self.characters

    def __repr__(self) -> str:
        return f'<{self.__module__}.Alphabet({self.characters}), {hex(id(self))}>'

    def __str__(self) -> str:
        nt = sorted([str(x) for x in self.nonterminals])
        t = sorted([str(x) for x in self.terminals])
        return f'Alphabet(N={nt}, T={t})'

    def __eq__(self, __x: object) -> bool:
        return (isinstance(__x, self.__class__)
                and __x.nonterminals == self.nonterminals
                and __x.terminals == self.terminals)

    def __hash__(self) -> int:
        return hash(self.value)
