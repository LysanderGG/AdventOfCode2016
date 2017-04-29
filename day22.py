import re
import itertools


regex = re.compile("/dev/grid/node-x(\d+)-y(\d+)\s*(\d+)T\s*(\d+)T\s*(\d+)T\s*(\d+)%")

class Node:
    def __init__(self, size, used, avail):
        self._size = size
        self._used = used
        self._avail = avail

    @property
    def used(self):
        return self._used

    @property
    def avail(self):
        return self._avail



def read_input(filepath):
    res = []
    with open(filepath) as f:
        for line in f:
            m = regex.match(line.strip())
            if m:
                elem = (int(m.group(1)), 
                        int(m.group(2)),
                        Node(int(m.group(3)), int(m.group(4)), int(m.group(5))))
                res.append(elem)
    return res


def count_viable_pairs(nodes):
    return sum(1 for (a, b) in itertools.permutations(nodes, 2) if a[2].used > 0 and a[2].used <= b[2].avail)


#def solve(nodes):
#    paths = []
#    goal = (0, max(y for (x, y, _) in nodes if x == 0))
#    while goal != (0, 0):
#
#    return paths


if __name__ == "__main__":
    nodes = read_input("day22.txt")
    nb_viable_pairs = count_viable_pairs(nodes)

    print("Part1: {}".format(nb_viable_pairs))

    #paths = solve(nodes)
    #print("Part2: {}".format(ans))
