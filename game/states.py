from typing import Tuple

GLIDER = {(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)}
OCTAGON2 = {
    (1, 2), (7, 3), (4, 7), (2, 6), (5, 1), (3, 0), (5, 6), (2, 1),
    (7, 4), (1, 5), (6, 2), (0, 4), (3, 7), (0, 3), (6, 5), (4, 0)
}
PULSAR = {
    (5, 9), (4, 7), (7, 3), (3, 0), (8, 0), (0, 7), (4, 12), (2, 12),
    (3, 7), (2, 5), (0, 3), (8, 5), (12, 9), (5, 8), (4, 0), (7, 2),
    (12, 2), (9, 0), (10, 7), (10, 12), (7, 10), (10, 0), (12, 10),
    (12, 3), (9, 7), (5, 4), (4, 5), (8, 7), (0, 8), (5, 3), (0, 1),
    (2, 7), (3, 5), (7, 8), (3, 12), (5, 10), (7, 9), (8, 12), (10, 5),
    (7, 4), (2, 0), (12, 4), (0, 9), (9, 5), (5, 2), (0, 2), (9, 12), (12, 8)
}


def generate_from_file(filepath: str) -> set:
    """
    Generate an initial state for the Game of Life from a pattern file from
    http://www.conwaylife.com/ wiki section (1.05 .lif version)

    Returns:
        set - a set of tuples (x, y) representing all the cells `alive` for the
        initial state.
    """
    DATA = set()
    with open(filepath) as fo:
        line_number_correction = 0
        for line_number, line in enumerate(fo.readlines()):
            # skip commented lines and adjust the line corrector value
            line = line.strip('\n')
            if line.startswith('#') or not line:
                line_number_correction -= 1
                continue

            for cn, c in enumerate(line):
                if c == '.':
                    continue
                xy = (line_number + line_number_correction, cn)
                DATA.add(xy)
    return DATA


def get_size(pattern: set) -> Tuple[int, int]:
    """Return the width and height of the pattern."""
    x = sorted(pattern, key=lambda t: t[0])
    y = sorted(pattern, key=lambda t: t[1])
    delta_x = x[-1][0] - x[0][0]
    delta_y = y[-1][1] - y[0][1]
    return delta_x, delta_y
