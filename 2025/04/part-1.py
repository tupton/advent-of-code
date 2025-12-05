import sys

# Tuples of (row, column) deltas for all 8 adjacent positions
adjacent_deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def main():
    lines = sys.stdin.readlines()
    grid = [list(line.strip()) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    assert all(len(row) == cols for row in grid), (
        "All rows must have the same number of columns"
    )

    accum = 0
    for row_num, row in enumerate(grid):
        for col_num, col in enumerate(row):
            if col == ".":
                continue
            if col == "@":
                occupied: list[bool] = []
                for dr, dc in adjacent_deltas:
                    adj_row, adj_col = row_num + dr, col_num + dc
                    if 0 <= adj_row < rows and 0 <= adj_col < cols:
                        if grid[adj_row][adj_col] == "@":
                            occupied.append(True)
                if len(occupied) < 4:
                    accum += 1

    print(f"Accessible paper rolls: {accum}")


if __name__ == "__main__":
    main()
