import unittest

from lsystem.model.symbol import Symbol
from lsystem.model.alphabet import Alphabet


class TestModelRule(unittest.TestCase):
    """ Test grammar alphabet. """

    def setUp(self) -> None:

        self.n1 = [Symbol(x) for x in 'AB']
        self.t1 = [Symbol(x) for x in 'ij']

        self.n2 = [Symbol(x) for x in 'ABCD']
        self.t2 = [Symbol(x) for x in 'abcd']

        self.n3 = [Symbol(x) for x in 'XYZ']
        self.t3 = [Symbol(x) for x in '123']

        self.alph1 = Alphabet(self.n1, self.t1)
        self.alph2 = Alphabet(self.n2, self.t2)
        self.alph3 = Alphabet(self.n3, self.t3)

    def test_constructor(self):
        """ Test if alphabet constructor raises TypeError for invalid types. """

        self.assertRaises(TypeError, Alphabet, ([1, 2, 3], self.t3))
        self.assertRaises(TypeError, Alphabet, (self.n1, ['i', 'j']))
        self.assertRaises(TypeError, Alphabet, (self.n2, 'abcd'))
        self.assertRaises(TypeError, Alphabet, ('XYZ', ['1', '2', '3']))

    def test_symbols(self):
        """ Test membership of symbols in the alphabet. """

        s1 = Symbol('A')
        s2 = Symbol('j')
        s6 = Symbol('1')

        self.assertTrue(self.alph1.is_nonterminal(s1))
        self.assertFalse(self.alph1.is_nonterminal(s2))

        self.assertTrue(self.alph1.is_terminal(s2))
        self.assertFalse(self.alph1.is_terminal(s6))

        self.assertFalse(self.alph2.is_nonterminal('1'))
        self.assertFalse(self.alph2.is_terminal('b'))

        self.assertFalse(self.alph3.is_terminal(1))
        self.assertFalse(self.alph3.is_terminal(2.5))

        result = (all(map(lambda x: x in self.alph2, self.n2))
                  and all(map(lambda x: x in self.alph2, self.t2)))
        self.assertTrue(result)

    def test_representation(self):
        """ Test printable output of an alphabet. """

        s = "Alphabet(N=['A', 'B'], T=['i', 'j'])"
        self.assertEqual(str(self.alph1), s)


if __name__ == "__main__":
    unittest.main()
