import sys

# Tuples of (row, column) deltas for all 8 adjacent positions
adjacent_deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def find_num_accessible_paper_rolls(grid: list[list[str]], accum: int = 0) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    assert all(len(row) == cols for row in grid), (
        "All rows must have the same number of columns"
    )
    new_grid: list[list[str]] = []
    for row_num, row in enumerate(grid):
        new_grid.append([])
        for col_num, col in enumerate(row):
            if col == ".":
                new_grid[row_num].append(".")
                continue
            if col == "@":
                occupied = sum(
                    1
                    for dr, dc in adjacent_deltas
                    if 0 <= row_num + dr < rows
                    and 0 <= col_num + dc < cols
                    and grid[row_num + dr][col_num + dc] == "@"
                )
                if occupied < 4:
                    new_grid[row_num].append(".")
                    accum += 1
                else:
                    new_grid[row_num].append("@")
    return (
        accum if grid == new_grid else find_num_accessible_paper_rolls(new_grid, accum)
    )


def main():
    lines = sys.stdin.readlines()
    grid = [list(line.strip()) for line in lines]

    accum = find_num_accessible_paper_rolls(grid)
    print(f"Accessible paper rolls: {accum}")


if __name__ == "__main__":
    main()
