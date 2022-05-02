from __future__ import annotations
from typing import Mapping, Union, overload


__all__ = ['LSystemState']


class LSystemState:

    @overload
    def __init__(self, state_dict: Mapping[str, int]) -> None:
        ...

    @overload
    def __init__(self, x: Union[int, float], y: Union[int, float], angle: Union[int, float]) -> None:
        ...

    def __init__(self, *args) -> None:

        if len(args) == 1 and isinstance(args[0], dict):
            self.x = args[0]['x']
            self.y = args[0]['y']
            self.angle = args[0]['angle']

        elif len(args) == 3 and all(map(lambda x: isinstance(x, (int, float)), args)):
            self.x = args[0]
            self.y = args[1]
            self.angle = args[2]

        else:
            raise NotImplementedError(
                f'InvalidArguments: LSystemState constructor does not support given argument types "{list(map(type, args))}".')

    def to_json(self) -> Mapping[str, int]:
        return {
            'x': self.x,
            'y': self.y,
            'angle': self.angle,
        }

    @classmethod
    def from_json(cls, state_dict: Mapping[str, int]) -> LSystemState:
        return LSystemState(state_dict)
