from __future__ import annotations
from typing import Tuple, List, TypeAlias

from dataclasses import dataclass, field

from lsystem.model.rule import Rule
from lsystem.model.symbol import Symbol
from lsystem.model.grammar import Grammar

from lsystem.mapping import InstructionMapping


@dataclass
class GrammarConfig:
    nonterminals: List[Symbol]
    terminals: List[Symbol]
    rules: List[Rule]
    axiom: Symbol


@dataclass
class StartingState:
    x: int
    y: int
    angle: int


@dataclass
class RendererConfig:
    line_segment_length: Pixels
    line_segment_length_reduction: Percentage
    angle_offset: Degrees

    instruction_mapping: InstructionMapping = field(default_factory=InstructionMapping.from_dict)

    starting_state: StartingState = field(default_factory=StartingState)


@dataclass
class LSystemConfig:
    name: str
    grammar: Grammar = field(default_factory=Grammar.from_dict)
    renderer_config: RendererConfig = field(default_factory=RendererConfig)


Pixels: TypeAlias = int
Percentage: TypeAlias = float
Degrees: TypeAlias = int


@dataclass
class GUIWindowConfig:
    window_size: Tuple[int, int] = field(default_factory=tuple)
    line_color: Tuple[int, int, int] = field(default_factory=tuple)
    background_color: Tuple[int, int, int] = field(default_factory=tuple)
