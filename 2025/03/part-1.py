import sys


def main():
    lines = sys.stdin.readlines()
    accum = 0
    for line in lines:
        digits = line.strip()
        # collect all possible pairs of digits in each line
        pairs: list[int] = []
        for i in range(0, len(digits) - 1):
            pairs += [
                int(digits[i]) * 10 + int(digits[i + j])
                for j in range(1, len(digits) - i)
            ]

        accum += max(pairs)

    print(f"Sum of max pairs: {accum}")


if __name__ == "__main__":
    main()
