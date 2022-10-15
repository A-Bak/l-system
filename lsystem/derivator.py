from __future__ import annotations
from typing import Union

from lsystem.model.grammar import Grammar
from lsystem.model.symbol import Symbol
from lsystem.model.word import Word


__all__ = ["GrammarDerivator"]


class GrammarDerivator:
    def __init__(self, grammar: Grammar) -> None:
        self.grammar = grammar
        self.word = grammar.axiom

    def next_derivation(self, w: Word) -> Union[Symbol, Word]:
        new_word = Word()

        for derivation in self.grammar.next_derivation(w):
            new_word.append(derivation)

        self.word = new_word
        return new_word

    def next_derivation_gen(self, w: Word) -> Union[Symbol, Word]:
        new_word = Word()

        for derivation in self.grammar.next_derivation(w):
            new_word.append(derivation)
            yield derivation

        self.word = new_word
