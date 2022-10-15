from __future__ import annotations
from lib2to3.pgen2 import grammar
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from lsystem.model.word import Word

import turtle

import hydra
import hydra.utils
from omegaconf import DictConfig
from lsystem.config import LSystemConfig, RendererConfig, GUIWindowConfig

from lsystem.model.grammar import Grammar
from lsystem.derivator import GrammarDerivator
from lsystem.renderer import TurtleRenderer


__all__ = ["LSystemGUI"]


HYDRA_CONFIG_PATH = "../../conf"


class LSystemGUI:
    def __init__(
        self,
        title: str,
        gui_config: GUIWindowConfig,
        derivator: GrammarDerivator,
        renderer: TurtleRenderer,
    ) -> None:

        self.screen = self._create_turtle_screen(
            title,
            gui_config.window_size,
            gui_config.line_color,
            gui_config.background_color,
        )

        self.derivator = derivator
        self.renderer = renderer

        self.display_word(self.derivator.word)

    def _create_turtle_screen(
        self,
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
        screen.onscreenclick(self._on_click)

        return screen

    def _on_click(self, pos_x: float, pos_y: float) -> None:
        self.display_word()

    def display_word(self, word: Word = None) -> None:

        displayed_word = (
            word
            if word is not None
            else self.derivator.next_derivation_gen(self.derivator.word)
        )

        self.screen.onscreenclick(None)
        self.renderer.draw(element=displayed_word, screen=self.screen)
        self.screen.onscreenclick(self._on_click)

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

    gui = LSystemGUI(
        title=lsystem_cfg.name,
        gui_config=gui_cfg,
        derivator=derivator,
        renderer=renderer,
    )


if __name__ == "__main__":

    main()
