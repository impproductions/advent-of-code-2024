from pathlib import Path
from math import prod

current_dir = Path(__file__).parent
input_file = Path(current_dir, "input.txt")

lines = input_file.read_text().splitlines()
tests = {
    (
        int(res),
        tuple(map(int, xpr.split())),
    )
    for res, xpr in (l.split(": ") for l in lines)
}


def eqs(res, xpr, ops, tot=0, pos=0):
    if pos >= len(xpr) - 1:
        return tot == res

    return any(eqs(res, xpr, ops, op((tot, xpr[pos + 1])), pos + 1) for op in ops)


def part1():
    return sum(res for res, xpr in tests if eqs(res, xpr, [sum, prod], xpr[0], 0))


def part2():
    cat = lambda nums: int(f"{nums[0]}{nums[1]}")
    return sum(res for res, xpr in tests if eqs(res, xpr, [sum, prod, cat], xpr[0], 0))


print(part1())
print(part2())
