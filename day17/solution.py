from dataclasses import dataclass
from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
a_val = int(lines[0].split(": ")[1])
b_val = int(lines[1].split(": ")[1])
c_val = int(lines[2].split(": ")[1])
program = list(map(int, lines[4].split(": ")[1].split(",")))


@dataclass
class Machine:
    P = 0
    A = 0
    B = 0
    C = 0
    OUT = []


M = Machine()


def cb(v):
    return v if v <= 3 else [M.A, M.B, M.C][v - 4]


def adv(o):
    M.A = M.A // (2 ** cb(o))


def bxl(o):
    M.B = M.B ^ o


def bst(o):
    M.B = cb(o) % 8


def jnz(o):
    if M.A == 0:
        return
    M.P = o
    M.P -= 2


def bxc(_):
    M.B = M.B ^ M.C


def out(o):
    M.OUT.append(cb(o) % 8)


def bdv(o):
    M.B = M.A // (2 ** cb(o))


def cfv(o):
    M.C = M.A // (2 ** cb(o))


instrs = [adv, bxl, bst, jnz, bxc, out, bdv, cfv]


def run(a, b, c, program):
    M.A, M.B, M.C, M.OUT, M.P = a, b, c, [], 0

    while M.P < len(program):
        instrs[program[M.P]](program[M.P + 1])
        M.P += 2


def part1():
    run(a_val, b_val, c_val, program)
    return ",".join(str(n) for n in M.OUT)


def part2():
    l, cursor = len(program), -1
    ta = 8 ** (l + cursor)  # let's give it a head start

    while abs(cursor) <= l:
        run(ta, 0, 0, program)

        if all(M.OUT[i] == program[i] for i in range(-1, cursor - 1, -1)):
            cursor -= 1
            continue

        ta += 8 ** (l + cursor)

    return ta


print(part1())
print(part2())
