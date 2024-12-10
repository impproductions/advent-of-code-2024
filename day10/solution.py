from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
size = len(lines)
map_ = {
    (x, y): int(lines[y][x])
    for x in range(size)
    for y in range(size)
}
starts = {p: v for p, v in map_.items() if v == 0}
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def count_trails(head, visited=None):
    if map_[head] == 9:
        if visited is None:
            return 1
        if not head in visited:
            visited.add(head)
            return 1
        else:
            return 0

    x, y = head
    nbs = [(x + dx, y + dy) for dx, dy in dirs]

    return sum(
        count_trails(nb, visited)
        for nb in nbs
        if nb in map_ and map_[nb] == map_[head] + 1
    )


def part1():
    return sum(count_trails(s, set()) for s in starts)


def part2():
    return sum(count_trails(s) for s in starts)


print(part1())
print(part2())
