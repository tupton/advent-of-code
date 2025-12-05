import sys

type Range = tuple[int, int]


def merge_or_append_range(merged_ranges: list[Range], current_range: Range) -> None:
    if not merged_ranges or len(merged_ranges) == 0:
        merged_ranges.append(current_range)
        return

    last_range = merged_ranges[-1]
    if current_range[0] >= last_range[0] and current_range[1] <= last_range[1]:
        print(f"  skipping range: {current_range}")
        return
    if current_range[0] <= last_range[1]:
        new_range: Range = (last_range[0], current_range[1])
        print(f"   merging range: {new_range}")
        merged_ranges[-1] = new_range
    else:
        print(f" appending range: {current_range}")
        merged_ranges.append(current_range)


def main():
    ranges: list[Range] = []
    for line in sys.stdin:
        if not line.strip():
            break
        start, end = map(int, line.strip().split("-", 1))
        ranges.append((start, end))

    merged_ranges: list[Range] = []
    for current_range in sorted(ranges, key=lambda r: r[0]):
        print(f"processing range: {current_range}")
        merge_or_append_range(merged_ranges, current_range)

    result = sum(end - start + 1 for start, end in merged_ranges)
    print(f"Ranges contain {result} IDs")


if __name__ == "__main__":
    main()
