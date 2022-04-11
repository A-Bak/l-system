
from lsystem.model.grammar import Grammar
from lsystem.model.symbol import Symbol
from lsystem.model.word import Word
from lsystem.model.rule import Rule

__all__ = ['LSystem']


class LSystem():

    def __init__(self) -> None:

        nt = [Symbol('F')]
        t = [Symbol('+-')]
        rule = Rule(Symbol('F'), Word('F+F−F−F+F'))

        self.grammar = Grammar(nt, t, [rule])

        self.axiom = 'F'
        # self.axiom = '''F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F+F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F−F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F−F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F+F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F'''

        self.instructions = {
            'F': None,
            '+': None,
            '-': None,
            '[': None,
            ']': None,
        }

        self.angle = 180
        self.length = 10

        pass

    def next_generation(self):
        pass
