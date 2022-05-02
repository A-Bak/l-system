import unittest

import os

from lsystem import LSystem
from lsystem.model.word import Word


class TestModelSymbol(unittest.TestCase):
    """ Test L-System. """

    def setUp(self) -> None:
        pass

    def test_constructor(self):
        """ Test LSystem constructor. """

        self.assertIsNotNone(LSystem.from_json(
            path_to_file='test/resources/lsystem_1.json'))

    def test_derivation(self):
        """ Test word derivations using LSystem's grammar. """

        lsystem = LSystem.from_json(
            path_to_file='test/resources/lsystem_1.json')

        self.assertEqual(lsystem.word, lsystem.grammar.axiom)
        self.assertEqual(lsystem.word, Word('A'))

        lsystem.next_derivation(lsystem.word)
        self.assertEqual(lsystem.word, Word('B+'))

        lsystem.next_derivation(lsystem.word)
        self.assertEqual(lsystem.word, Word('C-+'))

        lsystem.next_derivation(lsystem.word)
        self.assertEqual(lsystem.word, Word('D--+'))

        lsystem.next_derivation(lsystem.word)
        self.assertEqual(lsystem.word, Word('A+--+'))

    def test_derivation_gen(self):
        """ Test generator for word derivations using LSystem's grammar. """

        lsystem = LSystem.from_json(
            path_to_file='test/resources/lsystem_1.json')

    def test_json(self):
        """ Test serializing LSystem to and from JSON. """

        file_path = 'test/resources/lsystem_1.json'
        self.assertTrue(os.path.exists(file_path))

        with open(file_path, 'r') as f:
            json_string = f.read()

        ls1 = LSystem.from_json(path_to_file=file_path)
        ls2 = LSystem.from_json(s=json_string)

        self.assertIsNotNone(ls1)
        self.assertIsNotNone(ls2)
        self.assertEqual(ls1.grammar.alphabet, ls2.grammar.alphabet)
        self.assertEqual(ls1.grammar.axiom, ls2.grammar.axiom)

        for r1, r2 in zip(ls1.grammar.ruleset, ls2.grammar.ruleset):
            self.assertEqual(r1, r2)

        self.assertIsNotNone(ls1.to_json())

        ls1.to_json('test/resources/test.json')


if __name__ == "__main__":
    unittest.main()
