from typing import Tuple

import turtle

from lsystem import LSystemRenderer, LSystem


__all__ = ['LSystemGUI']


DEFAULT_WINDOW_SIZE = (800, 800)
DEFAULT_LINE_COLOR = (0, 0, 0)
DEFAULT_BACKGROUND_COLOR = (255, 255, 255)


class LSystemGUI():

    def __init__(self, lsystem: LSystem, renderer: LSystemRenderer,
                 window_size: Tuple[int, int] = DEFAULT_WINDOW_SIZE,
                 line_color: Tuple[int, int, int] = DEFAULT_LINE_COLOR,
                 background_color: Tuple[int, int, int] = DEFAULT_BACKGROUND_COLOR) -> None:

        self.lsystem = lsystem
        self.renderer = renderer

        self.start_state = renderer.current_state

        turtle.hideturtle()
        turtle.degrees(360)
        turtle.colormode(255)
        turtle.pencolor(line_color)
        turtle.tracer(5, 25)

        self.window = turtle.Screen()
        self.window.title('L-System')
        # self.window.setup(*window_size, *self.start_position)
        self.window.colormode(255)
        self.window.bgcolor(background_color)
        self.window.onscreenclick(self._on_click)

        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self._reset_turtle()

        self.display_word(lsystem.word)

        turtle.done()

    def display_word(self, word) -> None:
        self.window.onscreenclick(None)
        self.turtle.clear()
        self._reset_turtle()

        self.renderer.draw(word, self.turtle)

        self.window.onscreenclick(self._on_click)

    def _on_click(self, pos_x: float, pos_y: float) -> None:
        self.next_step()

    def next_step(self) -> None:
        self.window.onscreenclick(None)
        self.turtle.clear()
        self._reset_turtle()

        for derivation in self.lsystem.next_derivation(self.lsystem.word):

            self.renderer.draw(derivation, self.turtle)

        print(self.lsystem.word)

        self.window.onscreenclick(self._on_click)

    def _reset_turtle(self):
        self.turtle.penup()

        self.turtle.speed(0)
        self.turtle.setx(self.start_state.x)
        self.turtle.sety(self.start_state.y)
        self.turtle.seth(self.start_state.angle)

        self.turtle.pendown()


def load_lsystem(self):
    pass


def main():

    window_size = (800, 800)

    lsystem = LSystem.from_json(
        path_to_file='resources/dragon_curve.json')

    renderer = LSystemRenderer(lsystem)

    gui = LSystemGUI(lsystem, renderer)


if __name__ == '__main__':

    main()
