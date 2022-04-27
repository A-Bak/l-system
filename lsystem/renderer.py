from __future__ import annotations
from typing import Callable

from functools import singledispatchmethod
from turtle import Turtle

from lsystem.common import Instruction
from lsystem.lsystem import LSystem

from lsystem.model.symbol import Symbol
from lsystem.model.word import Word


__all__ = ['LSystemRenderer']


class LSystemRenderer():

    def __init__(self, lsystem: LSystem) -> None:
        self.angle_delta = lsystem.config.angle_offset
        self.position_delta = lsystem.config.segment_length
        self.length_reduction = lsystem.config.length_reduction

        self.current_state = lsystem.config.starting_state
        self.state_stack = []

        self.instruction_codes = {
            Instruction.forward: self._move_forward,
            Instruction.turn_right: self._turn_right,
            Instruction.turn_left: self._turn_left,
            Instruction.save_state: self._store_state,
            Instruction.load_state: self._load_state,
        }

        self.instruction_map = {symbol: self.instruction_codes[instruction_enum]
                                for symbol, instruction_enum in lsystem.instruction_mapping.items()}

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
        turtle_obj.forward(self.position_delta)

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

    def reduce_length(self) -> None:
        self.position_delta *= self.length_reduction
