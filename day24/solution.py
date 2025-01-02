from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
initial_wires, connections = input_file.read_text().split("\n\n")
initial_wires = [
    (l.split(": ")[0], int(l.split(": ")[1])) for l in initial_wires.splitlines()
]

connections = [
    (tuple(l.split(" -> ")[0].split(" ")), l.split(" -> ")[1])
    for l in connections.splitlines()
]

wires = {}
for (l, gate, r), t in connections:
    wires[l] = 0
    wires[r] = 0
    wires[t] = 0

for w, v in initial_wires:
    wires[w] = v

ops = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "XOR": lambda x, y: x ^ y,
}

connections = {w: (l, r, g) for (l, g, r), w in connections}


def calc(lg, rg, op):
    lv = wires[lg] if lg not in connections else calc(*connections[lg])
    rv = wires[rg] if rg not in connections else calc(*connections[rg])

    return ops[op](lv, rv)


def part1():
    zs = [(k, gate) for k, gate in connections.items() if k[0] == ("z")]
    res = [(w, calc(*gate)) for w, gate in zs]

    return int(("".join(str(r[1]) for r in sorted(res, reverse=True))), 2)


def part2():
    wrong = set()

    hz = "z" + str(max(int(w[1:]) for w in connections if w[0] == "z"))
    for w, (l, r, op) in connections.items():
        if w[0] == "z" and op != "XOR" and w != hz:
            wrong.add(w)

        # XOR gates should always involve an input or output bit
        if (
            op == "XOR"
            and w[0] not in "xyz"
            and l[0] not in "xyz"
            and r[0] not in "xyz"
        ):
            wrong.add(w)

        # AND gates should not feed into non-OR gates
        if op == "AND" and "x00" not in (l, r):
            for other_l, other_r, other_op in connections.values():
                if (w == other_l or w == other_r) and other_op != "OR":
                    wrong.add(w)

        # XOR gates should not feed into OR gates
        if op == "XOR":
            for other_l, other_r, other_op in connections.values():
                if (w == other_l or w == other_r) and other_op == "OR":
                    wrong.add(w)

    return ",".join(sorted(wrong))


print(part1())
print(part2())
