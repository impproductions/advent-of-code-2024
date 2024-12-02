from pathlib import Path

from functools import reduce

current_dir = Path(__file__).parent
input_file = Path(current_dir, "input.txt")

lines = input_file.read_text().splitlines()

levels = [list(map(int, l.split(" "))) for l in lines]

def is_safe(line):
    cmp = list(zip(line, line[1:]))
    asc = all(b >= a for a, b in cmp)
    desc = all(b <= a for a, b in cmp)
    dist = all(abs(a-b) in range(1, 4) for a, b in cmp)

    return (asc or desc) and dist

def part1():
    return sum(1 for l in levels if is_safe(l))

def part2():
    safe = 0

    for line in levels:
        if is_safe(line):
            safe += 1
            continue

        for y in range(len(line)):
            line2 = [l for j, l in enumerate(line) if j != y]
            if is_safe(line2):
                safe += 1
                break

    return safe

print(part1())
print(part2())