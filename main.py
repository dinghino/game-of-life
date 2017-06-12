import argparse
import sys
from typing import Tuple

import pygame
from game import game, states
from pygame.locals import QUIT

# =====================================================================
# Basic setup and constants


# -- PyGame constants -------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
CELL_SIZE = 8
FPS = 10

# -- Game of Life config ----------------------------------------------
DEFAULT_PATTERN = './game/patterns/124p37.lif'
ITERATIONS = 1000
GAME_PATTERN = states.generate_from_file(DEFAULT_PATTERN)
GAME_PATTERN_SIZE = states.get_size(GAME_PATTERN)

GAME_STATE = game.generate(GAME_PATTERN, ITERATIONS)

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
        x * CELL_SIZE + (WINDOW_WIDTH - GAME_PATTERN_SIZE[0] * CELL_SIZE) / 2,
        y * CELL_SIZE + (WINDOW_HEIGHT - GAME_PATTERN_SIZE[1] * CELL_SIZE) / 2
    )


def draw_cell(x: int, y: int) -> None:
    """Wrapper for the pygame.draw.rect call."""
    x, y = correct_coordinate(x, y)
    pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELL_SIZE, CELL_SIZE))


def quitter() -> None:
    pygame.quit()
    sys.exit()

# =====================================================================
# Game functions


def setup(pattern, iterations, fps):
    """
    Used to process argparse values overrides the global default configuration
    generating new values using the given parameters (if truthy).
    """
    global GAME_PATTERN
    global GAME_PATTERN_SIZE
    global GAME_STATE
    global ITERATIONS
    global FPS

    if pattern:
        GAME_PATTERN = states.generate_from_file(pattern)
        GAME_PATTERN_SIZE = states.get_size(GAME_PATTERN)
    if iterations:
        ITERATIONS = iterations
    if fps:
        FPS = fps

    if pattern or iterations:
        GAME_STATE = game.generate(GAME_PATTERN, ITERATIONS)


def main():
    """Main pygame loop."""
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pattern',
                        help='Path to the initial pattern.')

    parser.add_argument('-i', '--iterations', type=int,
                        help='Number of iterations to perform.')
    parser.add_argument('-f', '--fps', type=int,
                        help='Frames per seconds to render.')
    args = parser.parse_args()

    if args.pattern or args.iterations or args.fps:
        setup(args.pattern, args.iterations, args.fps)
    main()
