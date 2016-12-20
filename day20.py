import sys

blacklist = []
for line in open("day20.txt",'r'):
    range = tuple([int(e) for e in str.split(line, "-")])
    blacklist.append(range)


def check_first(l):
    i = 0
    for range in l:
        if i < range[0]:
            return i
        if range[0] <= i <= range[1]:
            i = range[1] + 1
    return i


def check_nb(l):
    nb_auth = 0
    i = 0
    for range in l:
        if i < range[0]:
            nb_auth += range[0] - i
            i = range[1] + 1
        if range[0] <= i <= range[1]:
            i = range[1] + 1

    # Handle the case where 4294967295 is not in the blacklist
    if i <= 4294967295:
        return nb_auth + (4294967295 - i + 1)

    return nb_auth

blacklist.sort()

print("Part1: first ip -", check_first(blacklist))
print("Part2: nb ips -", check_nb(blacklist))
