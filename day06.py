import collections


def read_input(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f]


def count_letters(filepath):
    words = read_input(filepath)
    size = len(words[0])
    counters = [collections.Counter() for _ in range(size)]
    for word in words:
        for idx, char in enumerate(word):
            counters[idx][char] += 1
    return counters


def most_common_chars_word(counters):
    return ''.join([c.most_common()[0][0] for c in counters])


def least_common_chars_word(counters):
    return ''.join([c.most_common()[::-1][0][0] for c in counters])


if __name__ == "__main__":
    counters = count_letters("day06.txt")

    ans = most_common_chars_word(counters)
    print("Part1: {}".format(ans))

    ans2 = least_common_chars_word(counters)
    print("Part2: {}".format(ans2))
