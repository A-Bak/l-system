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
        self.assertIsNotNone(Word())
        self.assertRaises(TypeError, Word, [1, 2, 3, 4])
        self.assertRaises(TypeError, Word, 110011)
        self.assertRaises(TypeError, Word, 101.01)

    def test_equals(self):
        """ Test equality of words. """
        self.assertEqual(Word(), Word())
        self.assertEqual(Word('ABAB'), self.w1)
        self.assertEqual(self.w1, self.w2)
        self.assertNotEqual(self.w1, self.w3)

    def test_append(self):
        """ Test extend for words - concatenation. """

        word = Word('X')
        word.append(self.w1)

        self.assertEqual(word, Word('XABAB'))
        self.assertEqual('XABAB', str(word))

        word = Word()
        word.append(self.w2)

        self.assertEqual(word, self.w2)
        self.assertEqual('ABAB', str(word))

    def test_representation(self):
        """ Test printable output of a word. """
        s = 'ABAB'
        self.assertEqual(s, str(self.w1))
        self.assertEqual(s, str(self.w2))

        self.assertEqual('', str(Word()))


if __name__ == "__main__":
    unittest.main()
