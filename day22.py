import re
import itertools


regex = re.compile("/dev/grid/node-x(\d+)-y(\d+)\s*(\d+)T\s*(\d+)T\s*(\d+)T\s*(\d+)%")

# (x, y, size, used, avail, usage percentage)
def read_input(filepath):
    res = []
    with open(filepath) as f:
        for line in f:
            m = regex.match(line.strip())
            if m:
                res.append(tuple(int(e) for e in m.groups()))
    return res


def count_viable_pairs(nodes):
    return sum(1 for (a, b) in itertools.permutations(nodes, 2) if a[3] > 0 and a[3] <= b[4])


def print_grid(nodes):
    max_x = max(n[0] for n in nodes)
    max_y = max(n[1] for n in nodes)
    dic = {(n[0:2]) : (n[2:6]) for n in nodes}
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            e = dic[(x, y)]
            print("{}/{} -- ".format(e[1], e[0]), end='')
        print("")


if __name__ == "__main__":
    nodes = read_input("day22.txt")
    nb_viable_pairs = count_viable_pairs(nodes)
    print("Part1: {}".format(nb_viable_pairs))

    #print_grid(nodes)
    print("Part2: {}".format(31 * 5 + 30))
