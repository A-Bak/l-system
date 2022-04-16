from enum import Enum

__all__ = ['InstructionEnum']


class Instruction(Enum):
    forward = "FORWARD"
    turn_left = "LEFT"
    turn_right = "RIGHT"
    save_state = "SAVE"
    load_state = "LOAD"
