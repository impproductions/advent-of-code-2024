from pathlib import Path
import re

current_dir = Path(__file__).parent
input_file = Path(current_dir, "input.txt")

text = input_file.read_text()

def parse(text):
    instr = re.findall(r"(mul\(\d+\,\d+\)|do\(\)|don't\(\))", text)
    res = []
    for t in instr:
        op, rest = t.split("(")
        res.append((op, *[int(d) for d in rest[:-1].split(",") if d]),)

    return res

def part1():
    return sum(t[1] * t[2] for t in parse(text) if t[0] == "mul")

def part2():
    enabled, tot = True, 0

    for t in parse(text):
        if t[0] == "mul" and enabled:
            tot += t[1] * t[2]
        else:
            enabled = True if t[0] == "do" else False

    return tot

print(part1())
print(part2())