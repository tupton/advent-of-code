import sys

def sort_lines(lines):
    return sorted([int(l) for l in lines if l])

def find_2020_pairs(ordered):
    pairs = []
    for i,n in enumerate(ordered):
        for r in reversed(ordered[i:]):
            if (n + r == 2020):
                pairs.append((n, r))
    return pairs
        
def mulitply_pairs(pairs):
    def multiply_tuple(p):
        x, y = p
        return x * y
    return map(multiply_tuple, pairs)


def find_2020_pair_and_multiply(input_file):
    lines = open(input_file).read().splitlines()
    ordered = sort_lines(lines)
    pairs = find_2020_pairs(ordered)
    multiplied = mulitply_pairs(pairs)
    print(list(multiplied))

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print('Usage: python find_2020_pair_and_multiply.py <input>')
        sys.exit(-1)

    find_2020_pair_and_multiply(sys.argv[1])
