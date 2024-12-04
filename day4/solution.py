from pathlib import Path

current_dir = Path(__file__).parent
input_file = Path(current_dir, "input.txt")

lines = input_file.read_text().splitlines()
size = len(lines)
points = tuple((x, y) for x in range(size) for y in range(size))

patterns1 = {
    ((0, 0), (1, 1), (2, 2), (3, 3)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (-1, 1), (-2, 2), (-3, 3)),
    ((0, 0), (-1, 0), (-2, 0), (-3, 0)),
    ((0, 0), (-1, -1), (-2, -2), (-3, -3)),
    ((0, 0), (0, -1), (0, -2), (0, -3)),
    ((0, 0), (1, -1), (2, -2), (3, -3)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
}

patterns2 = {
    ((-1, -1), (0, 0), (1, 1)),
    ((1, -1), (0, 0), (-1, 1)),
}


def is_(x, y, pattern, text, allow_reverse=False):
    mapped_pts = tuple(
        (x + x1, y + y1)
        for x1, y1 in pattern
        if (y + y1 in range(size) and x + x1 in range(size))
    )
    text = list(text)
    found = [lines[y][x] for x, y in mapped_pts]
    return found == text or (allow_reverse and text == found[::-1])


def part1():
    x_positions = [(x, y) for x, y in points if lines[y][x] == "X"]
    return sum(is_(x, y, patt, "XMAS") for patt in patterns1 for x, y in x_positions)


def part2():
    asc_p, desc_p = patterns2
    a_positions = [(x, y) for x, y in points if lines[y][x] == "A"]
    return sum(
        is_(x, y, asc_p, "MAS", allow_reverse=True)
        and is_(x, y, desc_p, "MAS", allow_reverse=True)
        for x, y in a_positions
    )


print(part1())
print(part2())
