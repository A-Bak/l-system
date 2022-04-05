from typing import Tuple

import pygame


class LSystemRenderer():

    def __init__(self, window_size: Tuple[int, int] = (600, 600)) -> None:

        pygame.init()

        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption("L-System")

    def render(self, lsystem=None):

        running = True
        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('Click')

        pygame.display.quit()
