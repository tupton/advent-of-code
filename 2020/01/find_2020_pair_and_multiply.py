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

def find_2020_triples(ordered):
    triples = []
    for i, n in enumerate(ordered):
        for j, m in enumerate(ordered[i:]):
            for k, l in enumerate(ordered[j:]):
                if (n + m + l == 2020):
                    triples.append((n, m, l))
    return triples
        
def mulitply_pairs(pairs):
    def multiply_pair(p):
        x, y = p
        return x * y
    return map(multiply_pair, pairs)

def multiply_triples(triples):
    def multiply_triple(t):
        x, y, z = t
        return x * y * z
    return map(multiply_triple, triples)

def find_2020_pair_and_multiply(input_file, group_size):
    lines = open(input_file).read().splitlines()
    ordered = sort_lines(lines)
    if group_size == 3:
        pairs = find_2020_triples(ordered)
    else:
        pairs = find_2020_pairs(ordered)

    if group_size == 3:
        multiplied = multiply_triples(pairs)
    else:
        multiplied = mulitply_pairs(pairs)

    print(list(multiplied))

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print('Usage: python find_2020_pair_and_multiply.py <input> [group_size]')
        sys.exit(-1)

    group_size = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    find_2020_pair_and_multiply(sys.argv[1], group_size)
