from pathlib import Path

current_dir = Path(__file__).parent
input_file = Path(current_dir, "input.txt")

lines = input_file.read_text().splitlines()
left = [int(l.split()[0]) for l in lines]
right = [int(l.split()[-1]) for l in lines]


def part1():
    l_s, r_s = list(sorted(left)), list(sorted(right))

    return sum([abs(l_s[i] - r_s[i]) for i in range(len(l_s))])

def part2():
    r_c = {}

    for r in right:
        r_c[r] = r_c.get(r, 0) + 1

    return sum(n * r_c.get(n, 0) for n in left)

print(part1())
print(part2())