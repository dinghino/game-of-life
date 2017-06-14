import sys
from typing import Tuple

import pygame
from pygame.locals import QUIT

from game import game, states
from viewer.config import (CELL_SIZE, DEFAULT_ITERATIONS, DEFAULT_PATTERN, FPS,
                           WINDOW_HEIGHT, WINDOW_SIZE, WINDOW_WIDTH)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# string constant used to render the iteration counter by counter_text()
COUNTER_STRING = '{0:0{2}d}/{1}'


class GameOfLife:
    def __init__(
        self,
        pattern=DEFAULT_PATTERN,
        iterations=DEFAULT_ITERATIONS,
        fps=FPS,
    ):
        self.pattern_path = pattern
        self.iterations = iterations
        self.current_iteration = 0

        # -- game of life init ----------------------------------------
        self.pattern = states.generate_from_file(pattern)
        self.pattern_width, self.pattern_height = states.get_size(self.pattern)
        self.game_state = game.generate(self.pattern, iterations)

        # -- pygame init ----------------------------------------------
        pygame.init()
        pygame.font.init()
        self.fps = fps
        self.timer = pygame.time.Clock()
        self.display = pygame.display.set_mode(WINDOW_SIZE)
        self.font = pygame.font.SysFont('monospace', 12)
        pygame.display.set_caption('Game of Life')

        # -- extra config ---------------------------------------------
        self.counter_zero_padding = len(str(iterations))

    # =================================================================
    # Utilities

    def correct_coordinates(self, x: int, y: int) -> Tuple[int, int]:
        """
        Adjust a cell's coordinates to be correctly displayed on the display.
        """
        x_center = (WINDOW_WIDTH - self.pattern_width * CELL_SIZE) / 2
        y_center = (WINDOW_HEIGHT - self.pattern_height * CELL_SIZE) / 2
        return (x * CELL_SIZE + x_center, y * CELL_SIZE + y_center)

    def draw_cell(self, x: int, y: int) -> None:
        """Wrapper for the pygame.draw.rect call."""
        x, y = self.correct_coordinates(x, y)
        pygame.draw.rect(
            self.display, WHITE,
            (x, y, CELL_SIZE, CELL_SIZE)
        )

    @property
    def counter_text(self) -> pygame.font:
        text = COUNTER_STRING.format(
            self.current_iteration,
            self.iterations,
            self.counter_zero_padding,
        )
        return self.font.render(text, 1, WHITE)

    def quitter(self) -> None:
        pygame.quit()
        sys.exit()

    # =================================================================
    # Game functions

    def run(self):
        while True:
            self.current_iteration += 1

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quitter()

            try:
                self.display.fill(BLACK)
                self.display.blit(self.counter_text, (10, 10))

                for x, y in next(self.game_state):
                    self.draw_cell(x, y)

            except StopIteration:
                self.quitter()

            pygame.display.update()
            self.timer.tick(self.fps)
