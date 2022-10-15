from __future__ import annotations
from typing import Callable, Union
from types import GeneratorType

from dataclasses import dataclass
from functools import singledispatchmethod

import turtle

from lsystem.config import RendererConfig
from lsystem.mapping import InstructionEnum

from lsystem.model.symbol import Symbol
from lsystem.model.word import Word


__all__ = ["TurtleRenderer", "RendererState"]


# TODO: Add incremental changes - length/angle changes per generation
#                               - length/angle changes per branch
#                               - change thickness and color?


@dataclass()
class RendererState:
    x: int
    y: int
    angle: int


class BaseRenderer:
    def __init__(
        self,
        config: RendererConfig,
        turtle_obj: turtle.Turtle = None,
    ) -> None:

        self.position_delta = config.line_segment_length
        self.angle_delta = config.angle_offset

        self.state_stack = []

        self.instruction_codes = {
            InstructionEnum.nop: self._nop,
            InstructionEnum.forward: self._move_forward,
            InstructionEnum.turn_right: self._turn_right,
            InstructionEnum.turn_left: self._turn_left,
            InstructionEnum.save_state: self._store_state,
            InstructionEnum.load_state: self._load_state,
        }

        self.instruction_map = {
            symbol: self.instruction_codes[instruction_enum]
            for symbol, instruction_enum in config.instruction_mapping.items()
        }

        if turtle_obj is None:
            self.turtle_obj = turtle.Turtle()
            self.turtle_obj.hideturtle()
        else:
            self.turtle_obj = turtle_obj

    def _interpret_instruction(self, symbol: Symbol) -> Callable[[None], None]:
        try:
            return self.instruction_map[symbol]
        except KeyError as e:
            raise ValueError(
                f'Invalid instruction mapping for symbol "{symbol}", not recognized.'
            ) from e

    def _nop(self) -> None:
        pass

    def _move_forward(self) -> None:
        self.turtle_obj.forward(self.position_delta)

    def _turn_right(self) -> None:
        self.turtle_obj.right(self.angle_delta)

    def _turn_left(self) -> None:
        self.turtle_obj.left(self.angle_delta)

    def _store_state(self) -> None:
        self.state_stack.append(self.current_state())

    def _load_state(self) -> None:
        state = self.state_stack.pop()

        self.turtle_obj.penup()
        self.turtle_obj.setposition(state.x, state.y)
        self.turtle_obj.setheading(state.angle)
        self.turtle_obj.pendown()

    def current_state(self) -> RendererState:
        return RendererState(
            self.turtle_obj.xcor(), self.turtle_obj.ycor(), self.turtle_obj.heading()
        )


class TurtleRenderer(BaseRenderer):
    def __init__(
        self,
        config: RendererConfig,
        turtle_obj: turtle.Turtle = None,
    ) -> None:
        super().__init__(config, turtle_obj)
        self.length_reduction = config.line_segment_length_reduction
        self.starting_state = config.starting_state

    def clear_canvas(self) -> None:
        self.turtle_obj.clear()
        self.turtle_obj.penup()
        self.turtle_obj.speed(0)
        self.turtle_obj.setx(self.starting_state.x)
        self.turtle_obj.sety(self.starting_state.y)
        self.turtle_obj.seth(self.starting_state.angle)
        self.turtle_obj.pendown()

    def draw(
        self,
        element: Union[Symbol, Word, GeneratorType],
        screen: turtle.TurtleScreen,
    ) -> None:
        self.clear_canvas()
        self._draw_element(element)
        screen.update()
        self.incremental_changes()

    @singledispatchmethod
    def _draw_element(self, element) -> None:
        raise NotImplementedError(
            f"Not supported type {type(element)} for LSystemRenderer._draw_element()."
        )

    @_draw_element.register
    def _(self, symbol: Symbol) -> None:
        instruction = self._interpret_instruction(symbol)
        instruction()

    @_draw_element.register
    def _(self, word: Word) -> None:
        for symbol in word:
            instruction = self._interpret_instruction(symbol)
            instruction()

    @_draw_element.register
    def _(self, derivation_gen: GeneratorType) -> None:
        for derivation in derivation_gen:
            self._draw_element(derivation)

    def incremental_changes(self) -> None:
        n = int(turtle.tracer() * 2)
        delay = int(turtle.delay() / 2)

        turtle.tracer(n, delay)

        self.position_delta *= self.length_reduction
