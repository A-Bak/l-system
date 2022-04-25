from __future__ import annotations
from typing import TYPE_CHECKING, Any, Mapping

from lsystem.model.symbol import Symbol
from lsystem.common import Instruction


__all__ = ['LSystemMapping']


class LSystemMapping:

    def __init__(self, instruction_mapping: Mapping[Symbol, Instruction]) -> None:
        self.mapping = instruction_mapping

    def to_json(self) -> Mapping[str, str]:
        return {str(key): str(value) for key, value in self.mapping.items()}

    @classmethod
    def from_json(cls, str_dict: Mapping[str, str]) -> LSystemMapping:
        instruction_mapping = {Symbol(key): Instruction.from_str(value)
                               for key, value in str_dict.items()}
        return LSystemMapping(instruction_mapping)
