import hashlib


def decode(input, pass_size):
    idx = 0
    pwd = ""
    while len(pwd) < pass_size:
        hash = hashlib.md5("{}{}".format(input, idx).encode()).hexdigest()
        if hash.startswith("00000"):
            pwd += hash[5]
            print("Current pwd {}".format(pwd))
        idx += 1
    return pwd


def decode2(input, pass_size):
    idx = 0
    pwd = '_' * pass_size
    while '_' in pwd:
        hash = hashlib.md5("{}{}".format(input, idx).encode()).hexdigest()
        if hash.startswith("00000"):
            pos = int(hash[5], 16)
            if pos < len(pwd) and pwd[pos] == '_':
                pwd = pwd[:pos] + hash[6] + pwd[pos + 1:]
                print("Current pwd {}".format(pwd))
        idx += 1
    return pwd


if __name__ == "__main__":
    input = "ojvtpuvg"

    #ans = decode(input, 8)
    #print("Part1: {}".format(ans))

    ans2 = decode2(input, 8)
    print("Part2: {}".format(ans2))
