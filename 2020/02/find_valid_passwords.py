import sys
import os
from collections import Counter

def validate(policies_and_passwords, policy_type):
    def validate_password_range_policy(policy_and_password):
        (policy, password) = policy_and_password
        (low, high, letter) = policy
        counts = Counter(list(password))
        letter_count = counts.get(letter, 0)
        return low <= letter_count <= high

    def validate_password_index_policy(policy_and_password):
        (policy, password) = policy_and_password
        (index1, index2, letter) = policy
        letter_at_index1 = list(password)[index1 - 1]
        letter_at_index2 = list(password)[index2 - 1]
        return (letter_at_index1 == letter) ^ (letter_at_index2 == letter)

    if policy_type == 'range':
        validator = validate_password_range_policy
    elif policy_type == 'index':
        validator = validate_password_index_policy

    return filter(validator, policies_and_passwords)

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

def find_valid_passwords(input_file, policy_type):
    lines = open(input_file).read().splitlines()
    policies_and_passwords = parse_lines(lines)
    valid_passwords = validate(policies_and_passwords, policy_type)

    print(len(list(valid_passwords)))

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f'Usage: python {os.path.basename(__file__)} <input> [policy_type]')
        sys.exit(-1)

    policy_type = sys.argv[2] if len(sys.argv) > 2 else 'range'

    find_valid_passwords(sys.argv[1], policy_type)

