import unittest

from lsystem.model.rule import Rule
from lsystem.model.symbol import Symbol
from lsystem.model.word import Word


class TestModelSymbol(unittest.TestCase):
    """ Test grammar symbol. """

    def setUp(self) -> None:

        self.s1 = Symbol('A')
        self.s2 = Symbol('A')

        self.s3 = Symbol('B')
        self.s4 = Symbol('ABC')

        self.w1 = Word('ABC')
        self.w2 = Word('ABA')

        self.rule1 = Rule(self.s3, self.w1)
        self.rule2 = Rule(self.s2, self.w2)

    def test_constructor(self):
        """ Test if constructor raises TypeError for invalid classes. """
        s = Symbol('A')
        self.assertEqual(s.value, 'A')

        self.assertRaises(TypeError, Symbol, (1))
        self.assertRaises(TypeError, Symbol, (0.25))
        self.assertRaises(TypeError, Symbol, (Rule))

    def test_equals(self):
        """ Test equality of symbols. """
        self.assertEqual(self.s1, self.s2)
        self.assertNotEqual(self.s1, self.s3)

    def test_apply_rule(self):
        """ Test applying rules on a symbol. """
        self.assertRaises(ValueError, self.s1.apply_rule, (self.rule1))

        result = Word([Symbol(x) for x in 'ABA'])
        self.assertEqual(result, self.s1.apply_rule(self.rule2))

    def test_apply_rule_result(self):
        """ Test if result of applying a rule is a word, not a symbol. """
        self.assertEqual(self.w1, self.s3.apply_rule(self.rule1))
        self.assertNotEqual(self.s4, self.s3.apply_rule(self.rule1))

    def test_representation(self):
        """ Test printable output of a symbol. """
        self.assertEqual(str(self.s1), 'A')
        self.assertEqual(str(self.s4), 'ABC')


if __name__ == "__main__":
    unittest.main()
