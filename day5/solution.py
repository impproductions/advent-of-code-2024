from pathlib import Path

current_dir = Path(__file__).parent
input_file = Path(current_dir, "input.txt")

sections = input_file.read_text().split("\n\n")
rules = [list(map(int, s.split("|"))) for s in sections[0].split("\n")]
updates = [list(map(int, u.split(","))) for u in sections[1].split("\n")]

ord = [
    sorted(
        row,
        key=lambda k: sum(1 for bef, aft in rules if aft == k and bef in set(row)),
    )
    for row in updates
]


def part1():
    return sum(u[len(u) // 2] for i, u in enumerate(updates) if u == ord[i])


def part2():
    return sum(ord[i][len(ord[i]) // 2] for i, u in enumerate(updates) if u != ord[i])


print(part1())
print(part2())
