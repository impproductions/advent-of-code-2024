import enum
from itertools import chain
from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
strdata = input_file.read_text()

blocks = list(map(int, strdata))
file_blocks = [[i // 2] * l for i, l in enumerate(blocks) if i % 2 == 0]
space_block = [["."] * l for i, l in enumerate(blocks) if i % 2 == 1]
if len(space_block) < len(file_blocks):
    space_block.append([])


def part1():
    file_bytes = list(chain(*file_blocks))
    arrng = []
    for i, l in enumerate(blocks):
        if l == 0:
            continue
        if i % 2 == 0:
            arrng.extend(file_bytes[:l])
            file_bytes = file_bytes[l:]
        else:
            arrng.extend(file_bytes[-1 : -l - 1 : -1])
            file_bytes = file_bytes[:-l]

    return sum(i * n for i, n in enumerate(arrng))


def part2():
    spaces = [len(sb) for sb in space_block]
    if len(spaces) < len(file_blocks):
        spaces.append(0)

    fb_c = len(file_blocks) - 1
    id_ = file_blocks[fb_c][0]
    while id_ >= 0:
        moved = False
        for sb_i in range(0, fb_c):
            if len(file_blocks[fb_c]) <= spaces[sb_i]:
                # move the last block
                cur = file_blocks.pop(fb_c)
                file_blocks.insert(sb_i + 1, cur)
                # merge the two spaces around the removed block
                spaces[fb_c - 1] += spaces.pop(fb_c) + len(cur)
                # resize space at insertion point
                spaces[sb_i] -= len(cur)
                # add zero-width space between adjacent ids (needed to reconstruct)
                spaces.insert(sb_i, 0)
                moved = True
                break
        # if the block under the cursor is moved back,
        # the next block to try is pushed forward
        if not moved: 
            fb_c -= 1
        id_ -= 1

    arrng = []
    for sb_i, fb in enumerate(file_blocks):
        arrng.extend(fb + [0] * spaces[sb_i])

    return sum(i * n for i, n in enumerate(arrng))


print(part1())
print(part2())
