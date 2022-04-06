

__all__ = ['LSystem']


class LSystem():

    def __init__(self) -> None:

        self.grammar = None
        # self.axiom = 'F[+F-F]F-FF[-F-F]F+F[+F-F]F-F+F'
        self.axiom = '''F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F+F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F−F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F−F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F+F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F'''

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
