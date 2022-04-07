from __future__ import annotations
from typing import List


import lsystem.model.alphabet as alphabet
import lsystem.model.symbol as symbol
import lsystem.model.word as word
import lsystem.model.rule as rule
import lsystem.model.ruleset as ruleset


__all__ = ['Grammar']


class Grammar:

    def __init__(self, nonterminals: List[symbol.Symbol], terminals: List[symbol.Symbol], rules: List[rule.Rule]) -> None:

        self.alphabet = alphabet.Alphabet(nonterminals, terminals)
        self.ruleset = ruleset.Ruleset(rules)

    def applicable_rules(self, s: symbol.Symbol) -> List[rule.Rule]:
        return [r for r in self.rules if r.is_applicable(s)]

    def add_nonterminal(self, s: symbol.Symbol) -> None:
        self.alphabet.add_nonterminal(s)

    def add_terminal(self, s: symbol.Symbol) -> None:
        self.alphabet.add_terminal(s)

    def add_rule(self, r: rule.Rule) -> None:
        self.ruleset.add_rule(r)

    def next_derivation(self, w: word.Word) -> word.Word:

        new_word = None

        for s in w:
            # Replace symbol with the application of a rule
            pass
