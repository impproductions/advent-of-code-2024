from collections import defaultdict
from pathlib import Path
from pprint import pprint

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
nums = list(map(int, lines))


def next(s):
    s = s ^ s << 6 & (2 << 23) - 1
    s = s ^ s >> 5 & (2 << 23) - 1
    s = s ^ s << 11 & (2 << 23) - 1

    return s


def part1():
    tot = 0
    for n in nums:
        for _ in range(2000):
            n = next(n)
        tot += n
    return tot


def part2():
    seqs_with_price = defaultdict(int)
    for n in nums:
        nxt, prev = n, None
        diffs, seen = [], set()
        for i in range(2001):
            if i >= 1:
                diffs.append(nxt % 10 - prev % 10)
            if i >= 4:
                seq = tuple(diffs[-5:-1])
                if seq not in seen:
                    seqs_with_price[seq] += prev % 10
                seen.add(seq)
            prev, nxt = nxt, next(nxt)
    return max(seqs_with_price.values())


print(part1())
print(part2())
