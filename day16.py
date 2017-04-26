def generate_data(s, length):
    while len(s) < length:
        s = s + '0' + ''.join(['1' if c == '0' else '0' for c in s[::-1]])
    return s[:length]


def checksum(s):
    while len(s) % 2 == 0:
        s = ''.join(['1' if s[i] == s[i+1] else '0' for i in range(0, len(s), 2)])
    return s


if __name__ == "__main__":
    ans = checksum(generate_data("11101000110010100", 272))
    print("Part1: {}".format(ans))

    ans = checksum(generate_data("11101000110010100", 35651584))
    print("Part2: {}".format(ans))