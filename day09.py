def read_input(filepath):
    with open(filepath) as f:
        return ''.join([line.strip() for line in f])


def decompress(input):
    output = ""
    while input:
        prev, _, input = input.partition('(')
        output += prev
        if input:
            marker, _, input = input.partition(')')
            nb_chars, nb_repeat = [int(_) for _ in marker.split('x')]
            output += input[:nb_chars] * nb_repeat
            input = input[nb_chars:]

    return output

def decompress_length(input):
    output_length = 0
    while input:
        prev, _, input = input.partition('(')
        output_length += len(prev)
        if input:
            marker, _, input = input.partition(')')
            nb_chars, nb_repeat = [int(_) for _ in marker.split('x')]
            repeat_string = input[:nb_chars]

            output_length += decompress_length(repeat_string) * nb_repeat
            input = input[nb_chars:]

    return output_length


if __name__ == "__main__":
    input = read_input("day09.txt")
    
    ans = len(decompress(input))
    print("Part1: {}".format(ans))

    ans2 = decompress_length(input)
    print("Part2: {}".format(ans2))
