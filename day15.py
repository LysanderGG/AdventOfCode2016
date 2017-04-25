def check_time(discs, time):
    for disc in discs:
        time += 1
        if (disc[1] + time) % disc[0] != 0:
            return False
    return True


def solve(discs):
    time = 0
    while True:
        if check_time(discs, time):
            return time
        time += 1


if __name__ == "__main__":
    discs = [(5, 2), (13, 7), (17, 10), (3, 2), (19, 9), (7, 0)]
    ans = solve(discs)
    print("Part1: {}".format(ans))

    discs = [(5, 2), (13, 7), (17, 10), (3, 2), (19, 9), (7, 0), (11, 0)]
    ans = solve(discs)
    print("Part2: {}".format(ans))
