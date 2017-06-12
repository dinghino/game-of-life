import sys
import pygame
from typing import Tuple
from pygame.locals import QUIT

from game import game, states

# =====================================================================
# Basic setup and constants


# -- PyGame constants -------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
CELL_SIZE = 8
FPS = 10

# -- Game of Life setup -----------------------------------------------
ITERATIONS = 1000
GAME_PATTERN = states.generate_from_file('./game/patterns/124p37.lif')
GAME_STATE = game.generate(GAME_PATTERN, ITERATIONS)

# NOTE that the duration of the game is (ITERATIONS / FPS) seconds

# =====================================================================
# Pygame setup


TIMER = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Game of Life')

pygame.init()

# =====================================================================
# Utilities


def correct_coordinate(x: int, y: int) -> Tuple[int, int]:
    """Adjust a cell's coordinates to be correctly displayed on the display."""
    return (
        x * CELL_SIZE + WINDOW_WIDTH / 2,
        y * CELL_SIZE + WINDOW_HEIGHT / 2
    )


def draw_cell(x: int, y: int) -> None:
    """Wrapper for the pygame.draw.rect call."""
    x, y = correct_coordinate(x, y)
    pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELL_SIZE, CELL_SIZE))


def quitter() -> None:
    pygame.quit()
    sys.exit()

# =====================================================================
# Game loop


while True:
    try:
        DISPLAYSURF.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                quitter()

        for x, y in next(GAME_STATE):
            draw_cell(x, y)

        TIMER.tick(FPS)
        pygame.display.update()

    except StopIteration:
        quitter()
