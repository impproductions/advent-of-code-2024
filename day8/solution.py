from pathlib import Path
from collections import defaultdict
from itertools import product, chain

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
size = len(lines)

map_ = {(x, y): lines[y][x] for y in range(size) for x in range(size)}
antennas = {
    a: [(x, y) for (x, y), f in map_.items() if f == a]
    for a in set(map_.values())
    if a != "."
}


def sign(x):
    return (x > 0) - (x < 0)


def get_antinodes(map_, p1, p2, start, amt=None):
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    antinodes = []

    i = start
    while (amt is None) or i < amt + start:
        x1a, y1a = x1 + (dx * i) * sign(x1 - x2), y1 + (dy * i) * sign(y1 - y2)
        x2a, y2a = x2 + (dx * i) * sign(x2 - x1), y2 + (dy * i) * sign(y2 - y1)
        if (x1a, y1a) in map_:
            antinodes.append((x1a, y1a))
        if (x2a, y2a) in map_:
            antinodes.append((x2a, y2a))
        i += 1

        if (x1a, y1a) not in map_ and (x2a, y2a) not in map_:
            break

    return antinodes


def calc(start, amt=None):
    ans = [
        get_antinodes(map_, p1, p2, start, amt)
        for positions in antennas.values()
        for p1, p2 in product(positions, repeat=2)
        if p1 != p2
    ]
    return len(set(chain.from_iterable(ans)))


def part1():
    return calc(1, 1)


def part2():
    return calc(0)


print(part1())
print(part2())
