from __future__ import annotations
from typing import Mapping, Tuple, overload

from lsystem.state import LSystemState


__all__ = ['LSystemConfig']


class LSystemConfig:

    @overload
    def __init__(self, angle_offset: int, segment_length: int, length_reduction: float, starting_state: LSystemState) -> None:
        ...

    @overload
    def __init__(self, dict: Mapping[str, int]) -> None:
        ...

    def __init__(self, *args) -> None:

        if len(args) == 1 and isinstance(args[0], dict):
            self.angle_offset = args[0]['angle_offset']
            self.segment_length = args[0]['segment_length']
            self.length_reduction = args[0]['length_reduction']
            self.starting_state = LSystemState(args[0]['starting_state'])

        elif len(args) == 3 and isinstance(args[1], int) and isinstance(args[2], int) and isinstance(args[3], LSystemState):
            self.angle_offset = args[0]
            self.segment_length = args[1]
            self.length_reduction = args[2]
            self.starting_state = args[3]

        else:
            raise NotImplementedError(
                f'InvalidArguments: LSystemConfig constructor does not support given arguments "{list(map(type, args))}".')

    def to_json(self) -> Mapping(str, int):
        return {'angle_offset': self.angle_offset,
                'segment_length': self.segment_length,
                'length_reduction': self.length_reduction,
                'starting_state': self.starting_state.to_json()}

    @classmethod
    def from_json(cls, config_dict: Mapping[str, int]):
        return LSystemConfig(config_dict)
