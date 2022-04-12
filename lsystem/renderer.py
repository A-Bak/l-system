from __future__ import annotations
from dis import Instruction
from typing import Callable, Tuple, Union

from functools import singledispatchmethod
from turtle import Turtle

from lsystem.model.symbol import Symbol
from lsystem.model.word import Word

__all__ = ['LSystemRenderer']


class LSystemState:

    def __init__(self, location: Tuple[int, int], angle: int) -> None:
        self.x = location[0]
        self.y = location[1]
        self.angle = angle


# TODO Saving and loading instruction map through LSystem

# TODO Shortening of edges with - subsequent steps ?
#                               - branching ?


class LSystemRenderer():

    def __init__(self, starting_state: LSystemState, location_delta: int = None, angle_delta: int = None) -> None:

        self.current_state = starting_state

        self.location_delta = location_delta
        self.angle_delta = angle_delta

        self.state_stack = []

        self.instruction_map = {
            Symbol('F'): self._move_forward,
            Symbol('G'): self._move_forward,
            Symbol('+'): self._turn_right,
            Symbol('-'): self._turn_left,
            Symbol('−'): self._turn_left,
            Symbol('['): self._store_state,
            Symbol(']'): self._load_state,
        }

    @singledispatchmethod
    def draw(self, other, turtle_obj: Turtle):
        raise NotImplementedError(
            f'Not supported type {type(other)} for LSystemRenderer.draw().')

    @draw.register
    def _(self, symbol: Symbol, turtle_obj: Turtle):
        instruction = self.interpret_instruction(symbol)
        instruction(turtle_obj)

    @draw.register
    def _(self, word: Word, turtle_obj: Turtle):
        for symbol in word:
            instruction = self.interpret_instruction(symbol)
            instruction(turtle_obj)

    def interpret_instruction(self, symbol: Symbol) -> Callable[[Turtle], None]:
        try:
            return self.instruction_map[symbol]
        except KeyError:
            raise ValueError(
                f'Invalid instruction mapping for symbol "{symbol}", not recognized.')

    def _move_forward(self, turtle_obj: Turtle) -> None:
        turtle_obj.forward(self.location_delta)

    def _turn_right(self, turtle_obj: Turtle) -> None:
        turtle_obj.right(self.angle_delta)

    def _turn_left(self, turtle_obj: Turtle) -> None:
        turtle_obj.left(self.angle_delta)

    def _store_state(self, turtle_obj: Turtle) -> None:
        self.state_stack.append(self.current_state)

    def _load_state(self, turtle_obj: Turtle) -> None:
        self.current_state = self.state_stack.pop()

        turtle_obj.penup()
        turtle_obj.setposition(self.current_state.x, self.current_state.y)
        turtle_obj.setheading(self.current_state.angle)
        turtle_obj.pendown()
