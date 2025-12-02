import sys


def main():
    lines = sys.stdin.readlines()
    dial = 50
    passed_zero = 0
    for line in lines:
        direction = line[0]
        amount = line[1:].strip()
        print(f"Direction: {direction}, Amount: {amount}")
        match direction:
            case "L":
                for i in range(int(amount)):
                    dial -= 1
                    if dial == 0:
                        passed_zero += 1
                    if dial < 0:
                        dial += 100

            case "R":
                for i in range(int(amount)):
                    dial += 1
                    if dial == 100:
                        passed_zero += 1
                    if dial > 99:
                        dial -= 100

            case _:
                raise ValueError(f"Unknown direction: {direction}")

    print(f"Landed on or passed zero {passed_zero} times.")


if __name__ == "__main__":
    main()
