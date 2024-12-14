from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
robots = [
    tuple(tuple(map(int, (p.split("=")[1].split(",")))) for p in l.split(" "))
    for l in lines
]


def print_map(pts):
    t = ""
    for y in range(103):
        for x in range(101):
            if (x, y) in pts:
                t += "#"
            else:
                t += "."
        t += "\n"
    return t


def part1():
    runs, h, w = 100, 103, 101
    mh, mw = h // 2, w // 2
    q1, q2, q3, q4 = [], [], [], []
    for (x, y), (vx, vy) in robots:
        x, y = ((x + vx * runs) % w, (y + vy * runs) % h)
        if x in range(mw) and y in range(mh):
            q1.append((x, y))
        elif x in range(mw + 1, w) and y in range(mh):
            q2.append((x, y))
        elif x in range(mw) and y in range(mh + 1, h):
            q3.append((x, y))
        elif x in range(mw + 1, w) and y in range(mh + 1, h):
            q4.append((x, y))

    return len(q1) * len(q2) * len(q3) * len(q4)


def part2():
    i = 0
    while True:
        h, w = 103, 101
        f_pos = set(
            [((x + vx * i) % w, (y + vy * i) % h) for (x, y), (vx, vy) in robots]
        )

        m = print_map(f_pos)
        if "###########" in m:
            break
        i += 1

    return i


print(part1())
print(part2())
