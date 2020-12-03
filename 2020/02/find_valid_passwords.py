import sys
import os
from collections import Counter

def validate(policies_and_passwords):
    def validate_password(policy_and_password):
        (policy, password) = policy_and_password
        (low, high, letter) = policy
        counts = Counter(list(password))
        letter_count = counts.get(letter, 0)
        return low <= letter_count <= high
    return filter(validate_password, policies_and_passwords)

def parse_password(password):
    return password.strip()

def parse_policy(policy):
    [low_high, letter] = policy.split(' ')
    [low, high] = low_high.split('-')
    return (int(low), int(high), letter)

def parse_lines(lines):
    def parse_line(line):
        [raw_policy, raw_password] = line.split(':')
        policy = parse_policy(raw_policy)
        password = parse_password(raw_password)
        return (policy, password)
    return map(parse_line, lines)

def find_valid_passwords(input_file):
    lines = open(input_file).read().splitlines()
    policies_and_passwords = parse_lines(lines)
    valid_passwords = validate(policies_and_passwords)
    print(len(list(valid_passwords)))

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f'Usage: python {os.path.basename(__file__)} <input>')
        sys.exit(-1)

    find_valid_passwords(sys.argv[1])

