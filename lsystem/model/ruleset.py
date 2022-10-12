from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from lsystem.model.symbol import Symbol

from random import choice
from collections import defaultdict

from lsystem.model.rule import Rule


__all__ = ["Ruleset"]


class Ruleset:
    def __init__(self, rules: List[Rule] = None) -> None:

        self.rule_dict = defaultdict(list)

        if rules is not None:
            for r in rules:
                self.add_rule(r)

    def add_rule(self, r: Rule) -> None:

        if not isinstance(r, Rule):
            raise TypeError(f"Invalid type for {r}, input must be of type Rule.")

        self.rule_dict[r.left_side].append(r)

    def all_applicable_rules(self, s: Symbol) -> List[Rule]:
        return self.rule_dict[s]

    def random_applicable_rule(self, s: Symbol) -> Rule:
        return choice(self.rule_dict[s]) if self.rule_dict[s] else None

    def __iter__(self) -> Rule:
        for rule_list in self.rule_dict.values():
            yield from rule_list
