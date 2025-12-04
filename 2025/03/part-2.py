import sys


def find_digit(bank: str, target_len: int, current_number: str) -> str:
    if target_len == 0:
        return current_number

    print(f"Searching for length {target_len} in bank: {bank}")

    # return the rest of the bank if its length matches target_len
    if len(bank) == target_len:
        print(
            f"Target length {target_len} matches remaining bank; taking the rest: {bank}"
        )
        return current_number + bank

    for i in range(9, 0, -1):
        remaining_len = len(bank) - target_len + 1
        for j, char in enumerate(bank[:remaining_len]):
            if char == str(i):
                print(
                    f"Found digit {char} at position {j} (remaining length {target_len})"
                )
                next_number = current_number + char
                return find_digit(bank[j + 1 :], target_len - 1, next_number)
    return current_number


def main():
    lines = sys.stdin.readlines()
    accum = 0
    for line in lines:
        bank = line.strip()
        max_number = find_digit(bank, 12, "")
        print(f"Max 12-tuple from bank {bank} is {max_number}")

        accum += int(max_number)

    print(f"Sum of max 12-tuples: {accum}")


if __name__ == "__main__":
    main()
