from heapq import heapify, heappop, heappush
import math
from pathlib import Path
import pprint
import queue

touse = "input.txt"
input_file = Path(Path(__file__).parent, touse)
lines = input_file.read_text().splitlines()
obs = [tuple(int(v) for v in line.split(",")) for line in lines]
size = 7 if touse != "input.txt" else 71
limit = 12 if touse != "input.txt" else 1024
map_ = {(x, y) for y in range(size) for x in range(size)}
s, e = (0, 0), (size - 1, size - 1)
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra(map_, end, p, obs):
    visited, pq = set(), [(0, p)]
    heapify(pq)
    while len(pq) > 0:
        score, cur = heappop(pq)
        if cur == end:
            return score
        if cur in visited:
            continue
        visited.add(cur)

        x, y = cur
        for dx, dy in dirs:
            nb = (x + dx, y + dy)
            if nb in map_ and nb not in visited and nb not in obs:
                heappush(pq, (score + 1, nb))

    return None


def part1():
    return dijkstra(map_, e, s, set(obs[:limit]))


def part2():
    l, r = limit, len(obs) - 1
    while l <= r:
        m = (l + r) // 2
        score = dijkstra(map_, e, s, set(obs[: m + 1]))
        if score is None and l == r:
            return f"{obs[m][0]},{obs[m][1]}"
        elif score is None:
            r = m
        else:
            l = m + 1


print(part1())
print(part2())
