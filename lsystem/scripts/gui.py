from __future__ import annotations
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from lsystem.model.word import Word

import turtle

from lsystem import LSystemRenderer, LSystem


__all__ = ['LSystemGUI']


DEFAULT_WINDOW_SIZE = (800, 800)
DEFAULT_LINE_COLOR = (0, 0, 0)
DEFAULT_BACKGROUND_COLOR = (255, 255, 255)


class LSystemGUI():

    def __init__(self) -> None:

        self.screen = self.init_screen()

        # TODO: Unfinished:
        # file_path = 'resources/plant_edge_rewriting_1.json'

        # file_path = 'resources/dragon_curve.json'
        # file_path = 'resources/hexagonal_gosper_curve.json'
        # file_path = 'resources/quadratic_koch_island.json'
        # file_path = 'resources/sierpinsky_triangle.json'
        file_path = 'resources/squared_squares.json'

        self.lsystem = LSystem.from_json(path_to_file=file_path)

        self.renderer = LSystemRenderer(self.screen,
                                        self.lsystem.config,
                                        self.lsystem.instruction_mapping)

        self.display_word(self.lsystem.word)

    def init_screen(self,
                    window_size: Tuple[int, int] = DEFAULT_WINDOW_SIZE,
                    line_color: Tuple[int, int, int] = DEFAULT_LINE_COLOR,
                    background_color: Tuple[int, int, int] = DEFAULT_BACKGROUND_COLOR) -> turtle.TurtleScreen:

        turtle.hideturtle()
        turtle.degrees(360)
        turtle.colormode(255)
        turtle.pencolor(line_color)
        turtle.tracer(10, 25)

        screen = turtle.Screen()
        screen.title('L-System')
        # screen.setup(*window_size)
        screen.colormode(255)
        screen.bgcolor(background_color)
        screen.onscreenclick(self._on_click)

        return screen

    def _on_click(self, pos_x: float, pos_y: float) -> None:
        self.display_word()

    def display_word(self, word: Word = None) -> None:

        if word is None:
            word = self.lsystem.next_derivation(self.lsystem.word)

        self.screen.onscreenclick(None)
        self.renderer.draw(word)
        self.screen.onscreenclick(self._on_click)

        if word is not None:
            print(word)
        else:
            print(self.lsystem.word)

        turtle.done()


def main():

    window_size = (800, 800)

    gui = LSystemGUI()


if __name__ == '__main__':

    main()
