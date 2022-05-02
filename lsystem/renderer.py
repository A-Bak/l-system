from __future__ import annotations
import turtle
from typing import Callable, Union
from types import GeneratorType

from functools import singledispatchmethod
from turtle import Turtle, TurtleScreen

from lsystem.common import Instruction
from lsystem.config import LSystemConfig
from lsystem.mapping import LSystemMapping

from lsystem.model.symbol import Symbol
from lsystem.model.word import Word


__all__ = ['LSystemRenderer']


# TODO: Move turtle_obj into renderer -> init LSystem and LSystemRenderer in LSystemGUI constructor?
# TODO: Increase turtle.tracer() n with every step, reduce turtle.tracer() delay with every step

# TODO: Add incremental changes - length/angle changes per generation
#                               - length/angle changes per branch
#                               - change thickness and color?

class BaseRenderer:

    def __init__(self,
                 config: LSystemConfig,
                 instruction_mapping: LSystemMapping,
                 turtle_obj: Turtle = None) -> None:

        self.angle_delta = config.angle_offset
        self.position_delta = config.segment_length

        self.current_state = config.starting_state
        self.state_stack = []

        self.instruction_codes = {
            Instruction.nop: self._nop,
            Instruction.forward: self._move_forward,
            Instruction.turn_right: self._turn_right,
            Instruction.turn_left: self._turn_left,
            Instruction.save_state: self._store_state,
            Instruction.load_state: self._load_state,
        }

        self.instruction_map = {symbol: self.instruction_codes[instruction_enum]
                                for symbol, instruction_enum in instruction_mapping.items()}

        if turtle_obj is None:
            self.turtle_obj = turtle.Turtle()
            self.turtle_obj.hideturtle()
        else:
            self.turtle_obj = turtle_obj

    def _interpret_instruction(self, symbol: Symbol) -> Callable[[None], None]:
        try:
            return self.instruction_map[symbol]
        except KeyError:
            raise ValueError(
                f'Invalid instruction mapping for symbol "{symbol}", not recognized.')

    def _nop(self) -> None:
        pass

    def _move_forward(self) -> None:
        self.turtle_obj.forward(self.position_delta)

    def _turn_right(self) -> None:
        self.turtle_obj.right(self.angle_delta)

    def _turn_left(self) -> None:
        self.turtle_obj.left(self.angle_delta)

    def _store_state(self) -> None:
        self.state_stack.append(self.current_state)

    def _load_state(self) -> None:
        self.current_state = self.state_stack.pop()

        self.turtle_obj.penup()
        self.turtle_obj.setposition(self.current_state.x, self.current_state.y)
        self.turtle_obj.setheading(self.current_state.angle)
        self.turtle_obj.pendown()


class LSystemRenderer(BaseRenderer):

    def __init__(self,
                 screen: TurtleScreen,
                 config: LSystemConfig,
                 instruction_mapping: LSystemMapping,
                 turtle_obj: Turtle = None) -> None:
        super().__init__(config, instruction_mapping, turtle_obj)

        self.screen = screen
        self.config = config

    def clear_canvas(self) -> None:
        self.turtle_obj.clear()

        self.turtle_obj.penup()
        self.turtle_obj.speed(0)
        self.turtle_obj.setx(self.config.starting_state.x)
        self.turtle_obj.sety(self.config.starting_state.y)
        self.turtle_obj.seth(self.config.starting_state.angle)
        self.turtle_obj.pendown()

    def draw(self, element: Union[Symbol, Word, GeneratorType]) -> None:
        self.clear_canvas()
        self._draw_element(element)
        self.screen.update()

        self.incremental_changes()

    @singledispatchmethod
    def _draw_element(self, element) -> None:
        raise NotImplementedError(
            f'Not supported type {type(element)} for LSystemRenderer._draw_element().')

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
        self.position_delta *= self.config.length_reduction
