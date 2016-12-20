import sys

blacklist = []
for line in open("day20.txt",'r'):
    range = tuple([int(e) for e in str.split(line, "-")])
    blacklist.append(range)


def check_first(l):
    nb_auth = 0
    i = 0
    for range in l:
        if i < range[0]:
            return i
        if range[0] <= i <= range[1]:
            i = range[1] + 1
            continue
    return i


def check_nb(l):
    nb_auth = 0
    i = 0
    for range in l:
        if i < range[0]:
            nb_auth += 1
            i += 1
        if range[0] <= i <= range[1]:
            i = range[1] + 1
            continue

    if i <= 4294967295:
        return nb_auth + (4294967295 - i + 1)

    return nb_auth

blacklist.sort()

print("Part1: first ip -", check_first(blacklist))
print("Part2: nb ips -", check_nb(blacklist))
