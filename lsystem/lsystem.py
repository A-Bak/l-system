from __future__ import annotations
from typing import TYPE_CHECKING, Union, Any

if TYPE_CHECKING:
    from lsystem.common import FilePath

import json

from lsystem.config import LSystemConfig
from lsystem.mapping import LSystemMapping

from lsystem.model.grammar import Grammar
from lsystem.model.symbol import Symbol
from lsystem.model.word import Word
from lsystem.model.rule import Rule


__all__ = ['LSystem', 'LSystemJSONEncoder', 'LSystemJSONDecoder']


class LSystem:

    def __init__(self, grammar: Grammar, instruction_mapping: LSystemMapping, config: LSystemConfig) -> None:
        self.grammar = grammar
        self.instruction_mapping = instruction_mapping
        self.config = config
        self.word = grammar.axiom

    def next_derivation(self, w: Word) -> Union[Symbol, Word]:

        new_word = Word()

        for derivation in self.grammar.next_derivation(w):
            new_word.append(derivation)
            yield derivation

        self.word = new_word

    def to_json(self, path_to_file: FilePath = None) -> str:

        json_string = json.dumps(self, cls=LSystemJSONEncoder)

        if path_to_file is not None:
            with open(path_to_file, 'w') as f:
                f.write(json_string)

        return json_string

    @classmethod
    def from_json(cls, s: str = None, path_to_file: FilePath = None) -> LSystem:

        if s is not None:
            return json.loads(s, cls=LSystemJSONDecoder)

        elif path_to_file is not None:
            with open(path_to_file, 'r') as f:
                return json.load(f, cls=LSystemJSONDecoder)

        else:
            raise ValueError('''Failed to load LSystem from JSON,
                             no JSON string or FilePath to JSON file
                             were passed to LSystem.from_json().''')


class LSystemJSONEncoder(json.JSONEncoder):

    def default(self, o: LSystem) -> Any:

        if not isinstance(o, LSystem):
            raise TypeError(f'Invalid type {type(o)} for LSystemJSONEncoder.')

        nt_list = [str(symbol) for symbol in o.grammar.alphabet.nonterminals]
        t_list = [str(symbol) for symbol in o.grammar.alphabet.terminals]
        rule_list = [[str(r.left_side), str(r.right_side)]
                     for r in o.grammar.ruleset]
        axiom = str(o.grammar.axiom)

        lsystem_dict = {
            'grammar': {
                'nonterminals': nt_list,
                'terminals': t_list,
                'rules': rule_list,
                'axiom': axiom
            },
            'mapping': o.instruction_mapping.to_json(),
            'config': o.config.to_json()
        }

        return lsystem_dict


class LSystemJSONDecoder(json.JSONDecoder):

    def decode(self, s: str) -> LSystem:

        json_dict = json.loads(s)

        nonterminals = [Symbol(x)
                        for x in json_dict['grammar']['nonterminals']]
        terminals = [Symbol(x)
                     for x in json_dict['grammar']['terminals']]
        rules = [Rule(Symbol(l), Word(r))
                 for l, r in json_dict['grammar']['rules']]
        axiom = Word(json_dict['grammar']['axiom'])

        grammar = Grammar(nonterminals, terminals, rules, axiom)

        instruction_mapping = LSystemMapping.from_json(json_dict['mapping'])
        config = LSystemConfig(json_dict['config'])

        return LSystem(grammar, instruction_mapping, config)
