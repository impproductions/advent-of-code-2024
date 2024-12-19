from functools import cache
from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
patterns, designs = tuple(lines[0].split(", ")), lines[2:]


@cache
def combs(dsg, i):
    if i >= len(dsg):
        return 1
    return sum(combs(dsg, i + len(p)) for p in patterns if dsg[i : i + len(p)] == p)


def part1():
    return sum(combs(d, 0) > 0 for d in designs)


def part2():
    return sum(combs(d, 0) for d in designs)


print(part1())
print(part2())
