from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
size = len(lines)
mp = {(x, y): lines[y][x] for y in range(size) for x in range(size)}
start = tuple((p for p in mp if mp[p] in "S"))[0]
end = tuple((p for p in mp if mp[p] in "E"))[0]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def traverse(pos):
    visited = set()
    path = [pos]
    while pos != end:
        visited.add(pos)
        x, y = pos
        for dx, dy in dirs:
            next = (x + dx, y + dy)
            if mp.get(next) in ".E" and next not in visited:
                visited.add(next)
                path.append(next)
                pos = next
                break
    return path


def part1():
    path = traverse(start)

    ss = 0
    for i, p1 in enumerate(path):
        for j in range(i, len(path)):
            d = dist(path[j], p1)
            if d > 0 and d <= 2 and (j - i - d) >= 100:
                ss += 1

    return ss


def part2():
    path = traverse(start)

    ss = 0
    for i, p1 in enumerate(path):
        for j in range(i, len(path)):
            d = dist(path[j], p1)
            if d > 0 and d <= 20 and (j - i - d) >= 100:
                ss += 1

    return ss


print(part1())
print(part2())
