from collections import Counter
from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
stones = input_file.read_text().split(" ")
stones = list(map(int, stones))


def apply(s):
    if s == 0:
        return [1]
    as_str = str(s)
    if len(as_str) % 2 == 0:
        return [int(as_str[: len(as_str) // 2]), int(as_str[len(as_str) // 2 :])]
    return [s * 2024]


def blink(stones, amt):
    counts = Counter(stones)
    for _ in range(amt):
        updated = Counter()
        for n, cnt in counts.items():
            updated.update({un: ucnt * cnt for un, ucnt in Counter(apply(n)).items()})

        counts = updated

    return sum(counts.values())


def part1():
    return blink(stones, 25)


def part2():
    return blink(stones, 75)


print(part1())
print(part2())
