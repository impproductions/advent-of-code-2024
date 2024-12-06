from pathlib import Path
from pprint import pprint

current_dir = Path(__file__).parent
input_file = Path(current_dir, "input.txt")

lines = input_file.read_text().splitlines()
size = len(lines)
map_ = {(x, y): val for y, l in enumerate(lines) for x, val in enumerate(l)}
start_pos = [k for k in map_ if map_[k] == "^"][0]
visited = set()

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))


def next(pos, dir, map_):
    x, y = pos
    dx, dy = dirs[dir]
    nx, ny = (x + dx, y + dy)

    if not (nx in range(0, size) and ny in range(0, size)):
        return pos, dir, "done"
    if map_[(nx, ny)] == "#":
        return pos, (dir + 1) % 4, "turn"
    return (nx, ny), dir, "move"


def part1():
    p, d = start_pos, 0

    while True:
        visited.add(p)
        p, d, res = next(p, d, map_)
        if res == "done":
            break

    return len(visited)


def part2():
    tot = 0

    for vpos in visited:
        p, d, states = start_pos, 0, {}
        map_[vpos] = "#"
        while True:
            if states.get((p, d), 0) == 2:
                tot += 1
                break
            p, d, res = next(p, d, map_)
            states[(p, d)] = states.get((p, d), 0) + 1
            if res == "done":
                break
        map_[vpos] = "."

    return tot


print(part1())
print(part2())
