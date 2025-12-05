import sys

type Range = tuple[int, ...]


def is_id_in_range(id: int, range: Range) -> bool:
    return range[0] <= id <= range[1]


def main():
    ranges: list[Range] = []
    line = sys.stdin.readline()
    while line.strip() != "":
        ranges.append(tuple(map(int, line.strip().split("-", 2))))
        line = sys.stdin.readline()

    ingredient_ids = [int(id.strip()) for id in sys.stdin.readlines()]

    ids_in_range = {
        id for id in ingredient_ids for r in ranges if is_id_in_range(id, r)
    }

    print(f"Found {len(ids_in_range)} ingredient IDs in range")


if __name__ == "__main__":
    main()
