import itertools
from typing import Generator, Tuple


def neighbors(point: Tuple[int]) -> Generator[Tuple[int, int], None, None]:
    """Generate all neighboring cells from a (x, y) coordinates tuple."""
    x, y = point
    delta_orthogonal = ((1, 0), (-1, 0), (0, 1), (0, -1))
    delta_diagonal = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    for dx, dy in itertools.chain(delta_orthogonal, delta_diagonal):
        yield (x + dx, y + dy)


def next_state(state: set) -> set:
    """Evaluate the next state of the board by the previouse state."""
    new_state = set()
    temp_state = state | set(itertools.chain(*map(neighbors, state)))
    for point in temp_state:
        neigh = sum((neigh in state) for neigh in neighbors(point))
        if neigh == 3 or (neigh == 2 and point in state):
            new_state.add(point)
    return new_state


def generate(initial_state, iterations=100):
    """
    Generator function that performs <iterations> iterations following the
    conway's laws on the given initial_state and yields board states.
    """
    state = initial_state
    for _ in range(iterations):
        state = next_state(state)
        yield state
