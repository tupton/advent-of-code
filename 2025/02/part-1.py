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
            # check if string is a repeated pattern
            if str_i[:half_str_len] * 2 == str_i:
                accum += i
                print(f"Found repeated pattern: {i}")

    print(f"Total sum of repeated patterns: {accum}")


if __name__ == "__main__":
    main()
