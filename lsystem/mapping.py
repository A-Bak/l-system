from __future__ import annotations
from typing import Mapping

from enum import Enum

from lsystem.model.symbol import Symbol


__all__ = ["InstructionMapping", "InstructionEnum"]


class InstructionEnum(Enum):
    nop = "NOP"
    forward = "FORWARD"
    turn_left = "LEFT"
    turn_right = "RIGHT"
    save_state = "SAVE"
    load_state = "LOAD"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def from_str(cls, s: str) -> InstructionEnum:

        for value in cls:
            if s == str(value):
                return value

        raise ValueError(f"String {s} is not a valid value for Enum type Instruction.")


class InstructionMapping(dict):
    def __init__(self, *arg, **kw) -> None:
        super(InstructionMapping, self).__init__(*arg, **kw)

    @classmethod
    def from_dict(cls, map: Mapping[str, str]) -> InstructionMapping:
        instruction_mapping = {
            Symbol(key): InstructionEnum.from_str(value) for key, value in map.items()
        }
        return InstructionMapping(instruction_mapping)
