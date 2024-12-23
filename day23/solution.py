from collections import defaultdict
from pathlib import Path

input_file = Path(Path(__file__).parent, "input.txt")
lines = input_file.read_text().splitlines()
conn_map = defaultdict(set)
for l, r in [l.split("-") for l in lines]:
    conn_map[l].add(r)
    conn_map[r].add(l)


def grow_clusters(
    cluster: set, potential: set, excluded: set, conn_map: dict, found: list, size=None
) -> None:
    if size and len(cluster) == 3:  # p1
        found.append(cluster)
        return
    if not size and not potential and not excluded:  # p2
        found.append(cluster)
        return
    for pc in potential.copy():
        grow_clusters(
            cluster | {pc},  # grow cluster
            potential & conn_map[pc],  # restrict growth to connected nodes
            excluded & conn_map[pc],  # restrict excluded to connected nodes
            conn_map,
            found,
            size,
        )
        potential.remove(pc)  # we explored this pc for this cluster
        excluded.add(pc)  # don't revisit this node


def part1():
    clusters = []
    grow_clusters(set(), set(conn_map.keys()), set(), conn_map, clusters, size=3)
    return len([c for c in clusters if any(pc for pc in c if pc.startswith("t"))])


def part2():
    clusters = []
    grow_clusters(set(), set(conn_map.keys()), set(), conn_map, clusters)
    return ",".join(sorted(max(clusters, key=len)))


print(part1())
print(part2())
