import unittest

import os
import json

from lsystem import LSystem, LSystemJSONEncoder


class TestModelSymbol(unittest.TestCase):
    """ Test L-System. """

    def setUp(self) -> None:
        pass

    def test_constructor(self):

        # ls = LSystem()
        pass

    def test_json(self):

        file_path = 'resources/dragon_curve.json'
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

        ls1.to_json('resources/test.json')


if __name__ == "__main__":
    unittest.main()
