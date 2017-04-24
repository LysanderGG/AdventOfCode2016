import hashlib


def find_triplet(s):
    while(len(s) > 2):
        if s[0] == s[1] == s[2]:
            return s[0]
        s = s[1:]
    return None


def contains_quintuplet(s, c):
    return c * 5 in s


def compute_hash(salt, index, stretching=0):
    hash = hashlib.md5("{}{}".format(salt, index).encode()).hexdigest()
    for _ in range(0, stretching):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash


def get_hash(hashes, salt, index, stretching=0):
    l = len(hashes)
    if index >= l:
        for i in range(l, index + 1000):
            hashes.append(compute_hash(salt, i, stretching))

    return hashes[index]


def solve(salt, stretching=0):
    index = 0
    key_idx = 0
    hashes = []

    while(key_idx < 64):
        hash = get_hash(hashes, salt, index, stretching)
        c = find_triplet(hash)
        if c is not None and any(contains_quintuplet(get_hash(hashes, salt, verif_idx, stretching), c) for verif_idx in range(index + 1, index + 1001)):
            print("key#{} / hash#{}: {}".format(key_idx, index, hash))
            key_idx += 1
        index += 1
    return index - 1


if __name__ == "__main__":
    salt = "cuanljph"
    stretch_size = 2016
    
    ans = solve(salt)
    print("Part1: {}".format(ans))

    ans2 = solve(salt, stretch_size)
    print("Part2: {}".format(ans2))
