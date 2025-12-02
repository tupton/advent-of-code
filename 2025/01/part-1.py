import sys


def main():
    lines = sys.stdin.readlines()
    dial = 50
    accumulator = 0
    for line in lines:
        direction = line[0]
        amount = line[1:].strip()
        print(f"Direction: {direction}, Amount: {amount}")
        match direction:
            case "L":
                dial -= int(amount)
            case "R":
                dial += int(amount)
            case _:
                raise ValueError(f"Unknown direction: {direction}")

        # Calculate number of times landed on zero
        result = abs(dial) % 100
        if result == 0:
            accumulator += 1

    print(f"Landed on zero {accumulator} times.")


if __name__ == "__main__":
    main()
