from __future__ import annotations
from typing import List

from random import choice
from collections import defaultdict

import lsystem.model.rule as rule
import lsystem.model.symbol as symbol


__all__ = ['Ruleset']


class Ruleset():

    def __init__(self, rules: List[rule.Rule] = None) -> None:

        self.rule_dict = defaultdict(list)

        if rules is not None:
            for r in rules:
                self.add_rule(r)

    def add_rule(self, r: rule.Rule) -> None:

        if not isinstance(r, rule.Rule):
            raise TypeError(
                f'Invalid type for {r}, input must be of type Rule.')

        self.rule_dict[r.left_side].append(r)

    def all_applicable_rules(self, s: symbol.Symbol) -> List[rule.Rule]:
        return self.rule_dict[s]

    def random_applicable_rule(self, s: symbol.Symbol) -> rule.Rule:
        return choice(self.rule_dict[s]) if self.rule_dict[s] else None
