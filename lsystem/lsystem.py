from __future__ import annotations
from typing import Union


from lsystem.model.grammar import Grammar
from lsystem.model.symbol import Symbol
from lsystem.model.word import Word
from lsystem.model.rule import Rule

__all__ = ['LSystem']


class LSystem():

    def __init__(self) -> None:

        nt = [Symbol('F'), Symbol('G')]
        t = [Symbol('+'), Symbol('-')]
        rules = [
            Rule(Symbol('F'), Word('F−G+F+G−F')),
            Rule(Symbol('G'), Word('GG')),
        ]

        self.grammar = Grammar(nt, t, rules)

        self.axiom = Word('F−G−G')
        self.word = self.axiom

        self.instructions = {
            'F': None,
            '+': None,
            '-': None,
            '[': None,
            ']': None,
        }

        self.angle = 90
        self.length = 10

        pass

    def next_derivation(self, w: Word) -> Union[Symbol, Word]:

        new_word = Word()

        for derivation in self.grammar.next_derivation(w):
            new_word.append(derivation)
            yield derivation

        self.word = new_word
