from typing import Tuple

import pygame

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

        self.line_color = line_color
        self.background_color = background_color

        pygame.init()
        pygame.display.set_caption("L-System")

        self.window = pygame.display.set_mode(window_size)
        self.window.fill(self.background_color)
        pygame.display.flip()

    def run(self, lsystem=None):

        running = True
        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.next_step()

        pygame.display.quit()

    def next_step(self):

        word = self.lsystem.next_generation()


def load_lsystem(self):
    pass


def main():

    # Load LSystem from JSON and pass it to GUI
    # Initialize renderer

    # Draw Initial Axiom

    # Click -> Next_Step -> Click -> ...

    lsystem = LSystem()
    renderer = LSystemRenderer()

    gui = LSystemGUI(lsystem, renderer)
    gui.run()


if __name__ == '__main__':

    main()
