def print_map(map_, hls):
    tp = ""
    for y in range(size):
        for x in range(size):
            c = map_[(x,y)]
            for f in hls:
                c = "#" if f((x, y)) else c
            tp += c
        tp += "\n"

