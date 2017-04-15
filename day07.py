
def read_input(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f]


def split_inside_outside(str, start_char, end_char):
    outside = [] # list of substrings outside of the brackets
    inside = [] # list of substrings inside the brackets

    s = str
    while len(s) > 0:
        pre, _, s = s.partition(start_char)
        outside.append(pre)

        if len(s) > 0:
            hypernet, _, s = s.partition(end_char)
            inside.append(hypernet)

    return inside, outside


def is_ABBA(str):
    return str[0] == str[3] and str[1] == str[2] and str[0] != str[1]


def has_ABBA(str):
    return any(is_ABBA(str[i:i+4]) for i in range(0, len(str) - 3))


def support_TLS(str):
    inside, outside = split_inside_outside(str, '[', ']')
    return any(has_ABBA(o) for o in outside) and not any(has_ABBA(i) for i in inside)


def test_ABA_BAB(str, list):
    for i in range(0, len(str) - 2):
        slice = str[i:i+3]
        if slice[0] == slice[2]:
            bab = slice[1] + slice[0] + slice[1]
            if any(bab in s for s in list):
                return True
    return False


def support_SSL(str):
    inside, outside = split_inside_outside(str, '[', ']')
    return any(test_ABA_BAB(o, inside) for o in outside)


def count_TLS(ips):
    return sum(support_TLS(ip) for ip in ips)


def count_SSL(ips):
    return sum(support_SSL(ip) for ip in ips)

if __name__ == "__main__":
    ips = read_input("day07.txt")

    ans = count_TLS(ips)
    print("Part1: {}".format(ans))
    
    ans2 = count_SSL(ips)
    print("Part2: {}".format(ans2))
