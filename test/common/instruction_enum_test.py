import unittest

from lsystem.common.instruction_enum import Instruction


class TestInstructionEnum(unittest.TestCase):
    """ Test instruction enumerate. """

    def test_representation(self):
        """ Test printable output of a symbol. """

        self.assertEqual(str(Instruction.forward), "FORWARD")
        self.assertEqual(str(Instruction.turn_left), "LEFT")
        self.assertEqual(str(Instruction.turn_right), "RIGHT")
        self.assertEqual(str(Instruction.save_state), "SAVE")
        self.assertEqual(str(Instruction.load_state), "LOAD")

    def test_from_str(self):
        """ Test construction Instructions from string. """

        self.assertEqual(Instruction.forward, Instruction.from_str('FORWARD'))
        self.assertEqual(Instruction.turn_left, Instruction.from_str('LEFT'))
        self.assertEqual(Instruction.turn_right, Instruction.from_str('RIGHT'))
        self.assertEqual(Instruction.save_state, Instruction.from_str('SAVE'))
        self.assertEqual(Instruction.load_state, Instruction.from_str('LOAD'))
