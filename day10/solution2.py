from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
size = len(lines)
map_ = {(x, y): int(lines[y][x]) for x in range(size) for y in range(size)}
starts = {p: v for p, v in map_.items() if v == 0}
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def count_trails(head, visited=None):
    stack = [head]
    tot = 0
    while len(stack) > 0:
        cur = stack.pop()
        if map_[cur] == 9:
            if visited is None:
                tot += 1
            elif not cur in visited:
                visited.add(cur)
                tot += 1
            continue
        x, y = cur
        nbs = [(x + dx, y + dy) for dx, dy in dirs]
        nbs = [nb for nb in nbs if nb in map_ and map_[nb] == map_[cur] + 1]

        stack.extend(nbs)

    return tot


def part1():
    return sum(count_trails(s, set()) for s in starts)


def part2():
    return sum(count_trails(s) for s in starts)


print(part1())
print(part2())
