import unittest

from lsystem.model.word import Word
from lsystem.model.symbol import Symbol


class TestModelWord(unittest.TestCase):
    """ Test grammar word. """

    def setUp(self) -> None:

        self.w1 = Word('ABAB')
        self.w2 = Word([Symbol(x) for x in 'ABAB'])

        self.w3 = Word('AAA')

    def test_constructor(self):
        """ Test if constructors raises TypeError fo invalid types. """
        Word()
        self.assertRaises(TypeError, Word, [1, 2, 3, 4])
        self.assertRaises(TypeError, Word, 110011)
        self.assertRaises(TypeError, Word, 101.01)

    def test_equals(self):
        """ Test equality of words. """
        self.assertEqual(Word(), Word())
        self.assertEqual(Word('ABAB'), self.w1)
        self.assertEqual(self.w1, self.w2)
        self.assertNotEqual(self.w1, self.w3)

    def test_contains(self):
        """ Test membership of symbols in words. """
        self.assertFalse(Symbol('A') in Word())

        self.assertTrue(Symbol('A') in self.w1)
        self.assertTrue(Symbol('B') in self.w1)
        self.assertFalse(Symbol('C') in self.w1)
        self.assertFalse(Symbol('a') in self.w1)

    def test_iter(self):
        """ Test iterating over symbols of words. """
        for char, symbol in zip('ABAB', self.w1):
            self.assertEqual(char, str(symbol))

        for s in Word():
            raise ValueError('Empty word should not contain any symbols.')

    def test_representation(self):
        """ Test printable output of a word. """
        s = 'ABAB'
        self.assertEqual(s, str(self.w1))
        self.assertEqual(s, str(self.w2))

        self.assertEqual('', str(Word()))


if __name__ == "__main__":
    unittest.main()
