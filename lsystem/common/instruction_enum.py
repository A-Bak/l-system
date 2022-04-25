from __future__ import annotations
from enum import Enum


__all__ = ['Instruction']


class Instruction(Enum):
    forward = "FORWARD"
    turn_left = "LEFT"
    turn_right = "RIGHT"
    save_state = "SAVE"
    load_state = "LOAD"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def from_str(cls, s: str) -> Instruction:

        for value in cls:
            if s == str(value):
                return value

        raise ValueError(
            f'String {s} is not a valid value for Enum type Instruction.')
