from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
text = input_file.read_text()

machines = [m.split("\n") for m in text.split("\n\n")]
for i, m in enumerate(machines):
    machines[i][0] = [int(v[2:]) for v in m[0].split(": ")[1].split(", ")]
    machines[i][1] = [int(v[2:]) for v in m[1].split(": ")[1].split(", ")]
    machines[i][2] = [int(v[2:]) for v in m[2].split(": ")[1].split(", ")]


def compute(ax, bx, tx, ay, by, ty):
    return (
        (ty * bx - tx * by) / (bx * ay - ax * by),
        (ty * ax - tx * ay) / (ax * by - bx * ay),
    )


def part1():
    tot = 0
    for (ax, ay), (bx, by), (tx, ty) in machines:
        amul, bmul = compute(ax, bx, tx, ay, by, ty)
        if amul.is_integer() and bmul.is_integer() and (amul <= 100 and bmul <= 100):
            tot += amul * 3 + bmul

    return tot


def part2():
    tot = 0
    for (ax, ay), (bx, by), (tx, ty) in machines:
        amul, bmul = compute(ax, bx, tx + 10000000000000, ay, by, ty + 10000000000000)
        if amul.is_integer() and bmul.is_integer():
            tot += amul * 3 + bmul

    return tot


print(part1())
print(part2())
