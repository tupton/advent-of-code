import sys
from typing import NamedTuple


class Range(NamedTuple):
    start: int
    end: int


def parse_range(line: str) -> Range:
    start, end = map(int, line.strip().split("-", 1))
    return Range(start, end)


def merge_ranges(ranges: list[Range]) -> list[Range]:
    if not ranges:
        return []

    sorted_ranges = sorted(ranges, key=lambda r: r.start)
    merged_ranges: list[Range] = [sorted_ranges[0]]
    for current_range in sorted_ranges[1:]:
        last_range = merged_ranges[-1]
        if current_range.start <= last_range.end:
            new_range = Range(last_range.start, max(last_range.end, current_range.end))
            print(f"   merging: {new_range}")
            merged_ranges[-1] = new_range
        else:
            print(f" appending: {current_range}")
            merged_ranges.append(current_range)
    return merged_ranges


def main():
    ranges: list[Range] = []
    for line in sys.stdin:
        if not line.strip():
            break
        ranges.append(parse_range(line))

    merged_ranges = merge_ranges(ranges)

    result = sum(r.end - r.start + 1 for r in merged_ranges)
    print(f"Ranges contain {result} IDs")


if __name__ == "__main__":
    main()
