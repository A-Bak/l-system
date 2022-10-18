from __future__ import annotations
from typing import TYPE_CHECKING, Callable, Protocol, Tuple

if TYPE_CHECKING:
    from lsystem.model.word import Word

import turtle

import hydra
import hydra.utils
from omegaconf import DictConfig
from lsystem.config import LSystemConfig

from lsystem.derivator import GrammarDerivator
from lsystem.renderer import TurtleRenderer


__all__ = ["LSystemGUI"]


HYDRA_CONFIG_PATH = "../conf"


def create_turtle_screen(
    title: str,
    window_size: Tuple[int, int],
    line_color: Tuple[int, int, int],
    background_color: Tuple[int, int, int],
) -> turtle.TurtleScreen:

    turtle.hideturtle()
    turtle.degrees(360)
    turtle.colormode(255)
    turtle.pencolor(line_color)
    turtle.tracer(2, 100)

    screen = turtle.Screen()
    screen.title(title)
    screen.setup(*window_size)
    screen.colormode(255)
    screen.bgcolor(background_color)

    return screen


class LSystemWindow(Protocol):
    def onscreenclick(self, function: Callable) -> None:
        """Perform action on the canvas when clicked."""

    def onkeypress(self, function: Callable, key_symbol: str) -> None:
        """Perform action when the key_symbol key is pressed."""

    def update(self) -> None:
        """Perform update on the canvas."""


class LSystemGUI:
    def __init__(
        self,
        screen: LSystemWindow,
        derivator: GrammarDerivator,
        renderer: TurtleRenderer,
    ) -> None:

        self.screen = screen
        self.derivator = derivator
        self.renderer = renderer

        self.display_word(self.derivator.word)
        self.allow_actions()

    def _on_click(self, pos_x: float, pos_y: float) -> None:
        self.display_word()

    def _on_key_press(self) -> None:
        self.display_word()

    def stop_actions(self) -> None:
        self.screen.onscreenclick(None)
        self.screen.onkeypress(None, "space")

    def allow_actions(self) -> None:
        self.screen.onscreenclick(self._on_click)
        turtle.listen()
        self.screen.onkeypress(self._on_key_press, key="space")

    def display_word(self, word: Word = None) -> None:

        displayed_word = (
            word
            if word is not None
            else self.derivator.next_derivation_gen(self.derivator.word)
        )

        self.stop_actions()
        self.renderer.draw(element=displayed_word, screen=self.screen)
        self.allow_actions()

        if word is not None:
            print(f"{word}\n")
        else:
            print(f"{self.derivator.word}\n")

        turtle.done()


@hydra.main(version_base=None, config_path=HYDRA_CONFIG_PATH, config_name="config")
def main(config: DictConfig):

    lsystem_cfg: LSystemConfig = hydra.utils.instantiate(config["lsystem"])
    gui_cfg = config["app"]

    derivator = GrammarDerivator(lsystem_cfg.grammar)
    renderer = TurtleRenderer(lsystem_cfg.renderer_config)
    screen = create_turtle_screen(title=lsystem_cfg.name, **gui_cfg)

    gui = LSystemGUI(
        screen=screen,
        derivator=derivator,
        renderer=renderer,
    )


if __name__ == "__main__":
    main()
