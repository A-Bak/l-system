import unittest

from lsystem.model.rule import Rule
from lsystem.model.ruleset import Ruleset
from lsystem.model.word import Word
from lsystem.model.symbol import Symbol


class TestModelRuleset(unittest.TestCase):
    """ Test grammar rule. """

    def setUp(self) -> None:

        self.r1 = Rule(Symbol('A'), Word('AA'))
        self.r2 = Rule(Symbol('A'), Word('ABA'))
        self.r3 = Rule(Symbol('A'), Word('a'))
        self.r4 = Rule(Symbol('B'), Word('b'))

    def test_constructor(self):
        """ Test if constructor raises TypeError for invalid types. """

        Ruleset()
        rules = [Rule(Symbol('x'), Word('y'))]
        Ruleset(rules)

        self.assertRaises(TypeError, Ruleset, Rule(Symbol('x'), Word('y')))
        self.assertRaises(TypeError, Ruleset, ('X', 'XYX'))

    def test_add_rule(self):
        """ Test adding new rules to a ruleset."""

        rs = Ruleset()

        self.assertEqual([], rs.all_applicable_rules(self.r1.left_side))
        rs.add_rule(self.r1)
        self.assertEqual([self.r1], rs.all_applicable_rules(self.r1.left_side))
        self.assertNotEqual(
            [self.r2], rs.all_applicable_rules(self.r1.left_side))

        rs.add_rule(self.r2)
        rs.add_rule(self.r3)
        rs.add_rule(self.r4)

        self.assertEqual(3, len(rs.all_applicable_rules(Symbol('A'))))
        self.assertEqual(1, len(rs.all_applicable_rules(Symbol('B'))))

    def test_random_applicable_rule(self):
        """ Test getting a random word from ruleset."""

        rs = Ruleset([self.r4])

        self.assertEqual(self.r4, rs.random_applicable_rule(Symbol('B')))

    def test_iterating(self):
        """ Test iterating over a ruleset. """

        rs = Ruleset()

        for _ in rs:
            raise ValueError('Expected empty Ruleset.')

        rs.add_rule(self.r1)
        rs.add_rule(self.r2)
        rs.add_rule(self.r3)

        self.assertEqual(3, sum(1 for r in rs))

        rules = [self.r1, self.r2, self.r3]

        for a, b in zip(rules, rs):
            self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
