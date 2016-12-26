import sys
import re
from collections import Counter
from operator import itemgetter


def read_room_list(filepath):
    with open(filepath) as f:
        for line in f:
            m = re.search("([a-z\-]+)(\d+)\[(\w+)\]", line)
            name = ''.join([c for c in m.group(1) if c != '-'])
            number = int(m.group(2))
            checksum = m.group(3)
            yield (name, number, checksum)


def get_room_name(room): return room[0]
def get_room_id(room): return room[1]
def get_room_checksum(room): return room[2]


def is_real_room(room):
    most_common = Counter(get_room_name(room)).most_common()
    most_common.sort(key=itemgetter(0))
    most_common.sort(key=itemgetter(1), reverse=True)
    return get_room_checksum(room) == ''.join([a[0] for a in most_common[:5]])


def get_sum_real_rooms(room_list):
    id_sum = 0
    for room in room_list:
        if is_real_room(room):
            id_sum += get_room_id(room)
    return id_sum


def rotate_letter(l, i):
    return chr(ord('a') + ((ord(l) - ord('a') + i) % 26))


def find_secret_room(room_list, secret):
    for room in room_list:
        room_id = get_room_id(room)
        clear_name = ''.join([rotate_letter(c, room_id) for c in get_room_name(room)])
        if clear_name.startswith(secret):
            print(room)


room_list = list(read_room_list("day04.txt"))
print("Part 1:", get_sum_real_rooms(room_list))
print("Part 2:")
find_secret_room(room_list, "northpole")
