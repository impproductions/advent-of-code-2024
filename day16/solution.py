from heapq import heapify, heappop, heappush
import math
from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
size = len(lines)
mp = {(x, y): lines[y][x] for y in range(size) for x in range(size)}
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
scores_map = {}
for rot in range(4):
    for di, d in enumerate(dirs):
        scores_map[(rot, dirs[(rot) % 4])] = 1
        scores_map[(rot, dirs[(rot - 1) % 4])] = 1001
        scores_map[(rot, dirs[(rot + 1) % 4])] = 1001
        scores_map[(rot, dirs[(rot + 2) % 4])] = 2001
start, end = tuple(sorted([k for k, v in mp.items() if v in "ES"]))


def dijkstra(map_: dict, p: tuple[int, int], rot: int, best_score=None):
    visited = {(p, rot): math.inf for p in map_ for rot in range(4)}
    pq = [(0, p, rot, [p])]
    heapify(pq)
    in_shortest_paths = set()
    while len(pq) > 0:
        score, cur, rot, tail = heappop(pq)
        visited[(cur, rot)] = score
        x, y = cur
        nb_scores = [scores_map[(rot, d)] for d in dirs]
        nbs = [(x + dx, y + dy) for dx, dy in dirs]
        for rot, nb in enumerate(nbs):
            nb_score = score + nb_scores[rot]
            if visited[(nb, rot)] > nb_score and map_[nb] != "#":
                heappush(pq, (nb_score, nb, rot, tail + [nb]))

        if cur == end and best_score is None:
            best_score = score

        if cur == end and score == best_score:
            for p in tail:
                in_shortest_paths.add(p)

    return best_score, len(in_shortest_paths)


def part1and2():
    tot, in_shortest_paths = dijkstra(mp, start, 0)
    return tot, in_shortest_paths


print(part1and2())
