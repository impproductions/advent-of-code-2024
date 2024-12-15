import os
from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
text = input_file.read_text()
map_section, inst = text.split("\n\n")
map_lines_1 = map_section.splitlines()
map_lines_2 = [
    "".join(c + c if c in (".", "#") else ("[]" if c == "O" else c + ".") for c in s)
    for s in map_lines_1
]
size = len(map_lines_1)
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
inst = [dirs[">v<^".index(d)] for d in inst.replace("\n", "")]


def can_move(mp, p, d, to_move):
    if mp[p] == "#":
        return False

    if mp[p] == ".":
        return True

    (x, y), (dx, dy) = p, d
    nx, ny = n = (x + dx, y + dy)
    if mp[p] == "O":
        to_move.add(p)
        return can_move(mp, n, d, to_move)

    if mp[p] in "[]":
        to_move.add(p)
        res = True
        if dy != 0:
            other = -1 if mp[p] == "]" else 1
            to_move.add((x + other, y))
            res = can_move(mp, (nx + other, ny), d, to_move)
        return res and can_move(mp, n, d, to_move)

    return can_move(mp, n, d, to_move)


def play(mp, instrs):
    n = list({p: v for p, v in mp.items() if v == "@"}.keys())[0]
    for dx, dy in instrs:
        to_move = set((n,))
        if can_move(mp, n, (dx, dy), to_move):
            (x, y), tmp = n, {}
            n = (x + dx, y + dy)
            for pt in to_move:
                tmp[pt], mp[pt] = mp[pt], "."
            for px, py in to_move:
                mp[(px + dx, py + dy)] = tmp[(px, py)]
    return mp


def part1():
    mp = {(x, y): map_lines_1[y][x] for y in range(size) for x in range(size)}
    return sum([100 * y + x for (x, y), v in play(mp, inst).items() if v == "O"])


def part2():
    mp = {(x, y): map_lines_2[y][x] for y in range(size) for x in range(size * 2)}
    return sum([100 * y + x for (x, y), v in play(mp, inst).items() if v == "["])


print(part1())
print(part2())
