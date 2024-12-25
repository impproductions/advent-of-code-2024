from pathlib import Path
from itertools import product

input_file = Path(Path(__file__).parent, "input.txt").read_text()
schematics = [s.splitlines() for s in input_file.split("\n\n")]
locks = [s for s in schematics if all(p == "#" for p in s[0])]
keys = [s for s in schematics if all(p == "#" for p in s[-1])]
k_c = [[sum([c[i] == "#" for c in k]) for i in range(5)] for k in keys]
l_c = [[sum([c[i] == "#" for c in l]) for i in range(5)] for l in locks]


def part1():
    return sum(all(l[i] + k[i] <= 7 for i in range(5)) for l, k in product(l_c, k_c))


print(part1())
