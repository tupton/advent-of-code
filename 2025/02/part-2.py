import sys


def main():
    lines = sys.stdin.readlines()
    line = lines[0].strip()
    ranges = line.split(",")
    accum = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        print(f"Start: {start}, End: {end}")
        for i in range(start, end + 1):
            str_i = str(i)
            half_str_len = len(str_i) // 2
            for j in range(1, half_str_len + 1):
                pattern = str_i[:j]
                pattern_repetition = len(str_i) // j
                if pattern * pattern_repetition == str_i:
                    accum += i
                    print(f"Found repeated pattern: {i}")
                    break

    print(f"Total sum of repeated patterns: {accum}")


if __name__ == "__main__":
    main()
