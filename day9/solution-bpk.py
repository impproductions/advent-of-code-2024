import enum
from itertools import chain
from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
strdata = input_file.read_text()

data = []
lens = []

fblock = []
sblock = []
cur_id = 0
for i, d in enumerate(strdata):
    if i % 2 == 0:
        data.append([cur_id] * int(d))
        fblock.append([cur_id] * int(d))
        lens.append(int(d))
        cur_id += 1
    else:
        sblock.append(["."] * int(d))
        data.append(["."] * int(d))
        lens.append(int(d))
    

def part1():
    fs = list(chain(*fblock))
    arrng = []
    for i, l in enumerate(lens):
        if l == 0:
            continue
        if i % 2 == 0:
            arrng.extend(fs[:l])
            fs = fs[l:]
        else:
            arrng.extend(fs[-1 : -l - 1 : -1])
            fs = fs[:-l]

    return sum(i * n for i, n in enumerate(arrng))


def part2():
    spaces = [len(sb) for sb in sblock]
    ord = fblock[:]
    if len(spaces) < len(ord):
        spaces.append(0)

    sec = 0

    fs = list(chain(*fblock))
    id_ = max(fs)

    fidx = -1
    while True:
        sec += 1
        for i, fr in enumerate(ord):
            if len(fr) > 0 and fr[0] == id_:
                fidx = i

        for i in range(len(spaces)):
            if i >= fidx:
                break
            # if spaces[i] > 0:
            #     print("id", id_, "idx", fidx, len(ord[fidx]), "vs", spaces[i], "at", i)
            if spaces[i] == 0: 
                continue
            if len(ord[fidx]) <= spaces[i]:
                curl = len(ord[fidx])
                cur = ord[fidx]
                ord = ord[:fidx] + ord[fidx+1:]
                ord.insert(i+1, cur)
                spaces[i] -= curl
                spaces[fidx-1] += curl + spaces[fidx]
                spaces = spaces[:fidx] + spaces[fidx+1:]
                spaces.insert(i, 0)
                break
        id_ -= 1

        if id_ == 0:
            break

    arrng = []

    for i, num in enumerate(ord):
        arrng.extend(num)
        arrng.extend(["."]*spaces[i])

    return sum(i * n for i, n in enumerate(arrng) if n != ".")


print(part1())
print(part2())
