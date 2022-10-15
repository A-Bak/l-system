from __future__ import annotations
from typing import List, Union, Mapping

from lsystem.model.symbol import Symbol
from lsystem.model.word import Word
from lsystem.model.rule import Rule
from lsystem.model.alphabet import Alphabet
from lsystem.model.ruleset import Ruleset

__all__ = ["Grammar"]


class Grammar:
    def __init__(
        self,
        nonterminals: List[Symbol],
        terminals: List[Symbol],
        rules: List[Rule],
        axiom: Word,
    ) -> None:
        self.alphabet = Alphabet(nonterminals, terminals)
        self.ruleset = Ruleset(rules)
        self.axiom = axiom

    def applicable_rules(self, s: Symbol) -> List[Rule]:
        return [r for r in self.rules if r.is_applicable(s)]

    def add_nonterminal(self, s: Symbol) -> None:
        self.alphabet.add_nonterminal(s)

    def add_terminal(self, s: Symbol) -> None:
        self.alphabet.add_terminal(s)

    def add_rule(self, r: Rule) -> None:
        self.ruleset.add_rule(r)

    def apply_rule(self, s: Symbol) -> Word:
        return self.ruleset.random_applicable_rule(s).right_side

    def next_derivation(self, w: Word) -> Union[Symbol, Word]:
        for s in w:
            if s in self.alphabet.nonterminals:
                yield self.apply_rule(s)
            else:
                yield s

    @classmethod
    def from_dict(
        cls,
        nonterminals: List[str],
        terminals: List[str],
        rules: List[List[str]],
        axiom: str,
    ) -> Grammar:
        return Grammar(
            [Symbol(x) for x in nonterminals],
            [Symbol(x) for x in terminals],
            [Rule(Symbol(l), Word(r)) for l, r in rules],
            Word(axiom),
        )
