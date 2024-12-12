from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
size = len(lines)
mp = {(x, y): lines[y][x] for y in range(size) for x in range(size)}
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diags = [(1, 1), (-1, -1), (1, -1), (-1, 1)]


def grow(pos, ch, area, mp):
    if not pos in mp:
        return [pos]
    if pos in area:
        return []
    if ch != mp[pos]:
        return [pos]

    area.add(pos)
    x, y = pos
    perimeter = [p for dx, dy in dirs for p in grow((x + dx, y + dy), ch, area, mp)]

    return perimeter


def part1():
    explored = set()
    tot = 0
    area = set()
    to_see = [(0, 0)]

    while len(to_see) > 0:
        area = set()
        here = to_see.pop()
        if here in explored or not here in mp:
            continue
        perim = grow(here, mp[here], area, mp)
        tot += len(area) * len(perim)
        explored = explored | area
        to_see.extend(set(perim) - explored)

    return tot


def count_corners(x, y, region):
    return sum(
        ((x, y + dy) not in region and (x + dx, y) not in region)
        or (
            (x, y + dy) in region
            and (x + dx, y) in region
            and (x + dx, y + dy) not in region
        )
        for dx, dy in diags
    )


def part2():
    explored = set()
    tot = 0
    area = set()
    to_see = [(0, 0)]

    while len(to_see) > 0:
        area = set()
        here = to_see.pop()
        if here in explored or not here in mp:
            continue
        perim = grow(here, mp[here], area, mp)
        explored = explored | area
        to_see.extend(set(perim) - explored)

        tot_sides = 0
        for p in area:
            corners = count_corners(*p, area)
            tot_sides += corners
        tot += len(area) * tot_sides

    return tot


print(part1())
print(part2())
