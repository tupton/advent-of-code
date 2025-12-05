import sys
from typing import Final

type Grid = list[list[str]]
type Coordinates = tuple[int, int]

# Tuples of (row, column) deltas for all 8 adjacent positions
ADJACENT_DELTAS: Final[tuple[Coordinates, ...]] = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def remove_if_accessible(grid: Grid, row_num: int, col_num: int) -> str:
    """
    "Remove" (change from "@" to ".") a paper roll at (row_num, col_num) if it is accessible.

    A paper roll is considered accessible if it has fewer than 4 adjacent paper rolls.
    """
    if grid[row_num][col_num] == ".":
        return "."

    rows, cols = len(grid), len(grid[0]) if len(grid) > 0 else 0
    adjacent_count = sum(
        1
        for dr, dc in ADJACENT_DELTAS
        if 0 <= row_num + dr < rows
        and 0 <= col_num + dc < cols
        and grid[row_num + dr][col_num + dc] == "@"
    )
    return "." if adjacent_count < 4 else "@"


def regenerate_grid(grid: Grid) -> tuple[Grid, int]:
    """
    Generate a new grid after removing all accessible paper rolls from the input grid.

    Returns the new grid and the count of removed paper rolls.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    assert all(len(row) == cols for row in grid), (
        "All rows must have the same number of columns"
    )

    new_grid: Grid = [
        [remove_if_accessible(grid, row_num, col_num) for col_num in range(cols)]
        for row_num in range(rows)
    ]

    return new_grid, get_grid_removed_count(grid, new_grid)


def get_grid_removed_count(grid1: Grid, grid2: Grid) -> int:
    """
    Compare two grids and count how many paper rolls were removed from grid1 to grid2.
    A paper roll is considered removed if it was "@" in grid1 and "." in grid2.
    """
    return sum(
        1
        for row1, row2 in zip(grid1, grid2)
        for cell1, cell2 in zip(row1, row2)
        if cell1 != cell2 and cell2 == "."
    )


def find_num_accessible_paper_rolls(grid: Grid) -> int:
    """
    Recursively generate a new grid and accumulate the count of removed paper rolls until no more can be removed.
    """

    accum = 0

    while True:
        new_grid, changed_count = regenerate_grid(grid)

        accum += changed_count

        if new_grid == grid:
            return accum

        grid = new_grid


def main():
    grid: Grid = [list(line.strip()) for line in sys.stdin]

    num_accessible_paper_rolls = find_num_accessible_paper_rolls(grid)
    print(f"Accessible paper rolls: {num_accessible_paper_rolls}")


if __name__ == "__main__":
    main()
