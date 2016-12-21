import sys

#operation: (command, x, y)
operations = []
with open("day21.txt",'r') as f:
    for line in f:
        if line.startswith("swap position"):
            cmd = "swap position"
            x = int(line[len("swap position ")])
            y = int(line[len("swap position X with position ")])
        elif line.startswith("swap letter"):
            cmd = "swap letter"
            x = line[len("swap letter ")]
            y = line[len("swap letter X with letter ")]
        elif line.startswith("rotate left"):
            cmd = "rotate left"
            x = int(line[len("rotate left ")])
            y = 0
        elif line.startswith("rotate right"):
            cmd = "rotate right"
            x = int(line[len("rotate right ")])
            y = 0
        elif line.startswith("rotate based on position of letter"):
            cmd = "rotate pos"
            x = line[len("rotate based on position of letter ")]
            y = 0
        elif line.startswith("reverse positions"):
            cmd = "reverse positions"
            x = int(line[len("reverse positions ")])
            y = int(line[len("reverse positions X through ")])
        elif line.startswith("move position"):
            cmd = "move position"
            x = int(line[len("move position ")])
            y = int(line[len("move position X to position ")])
        else:
            assert(0)

        operations.append((cmd, x, y))


def swap_position(x, y, p):
    a, b = min(x,y), max(x,y)
    return p[:a] + p[b] + p[a+1:b] + p[a] + p[b+1:]


def swap_letter(x, y, p):
    new_p = ""
    for c in p:
        if c == x:
            new_p += y
        elif c == y:
            new_p += x
        else:
            new_p += c
    return new_p



def rotate_left(x, p):
    return p[x:] + p[:x]


def rotate_right(x, p):
    return rotate_left(-x, p)


def rotate_pos(x, p):
    if x not in p:
        return p

    i = p.index(x)
    if i >= 4:
        i += 1

    i = (i + 1) % len(p)
    return rotate_right(i, p)


def rotate_pos_reverse(x, p):
    new_p = p
    while True:
        new_p = rotate_left(1, new_p)
        i = new_p.index(x)
        if rotate_pos(x, new_p) == p:
            return new_p


def reverse_pos(x, y, p):
    a, b = min(x,y), max(x,y)
    min_idx = a-1 if a > 0 else 0
    return p[:a] + p[a:b+1][::-1] + p[b+1:]


def move_pos(x, y, p):
    l = p[x]
    if x < y:
        return p[:x] + p[x+1:y+1] + l + p[y+1:]
    else:
        return p[:y] + l + p[y:x] + p[x+1:]


def process_command(command, password, scramble_mode):
    cmd, x, y = command

    if cmd == "swap position":
        password = swap_position(x, y, password)
    elif cmd == "swap letter":
        password = swap_letter(x, y, password)
    elif cmd == "rotate left":
        if scramble_mode:
            password = rotate_left(x, password)
        else:
            password = rotate_right(x, password)
    elif cmd == "rotate right":
        if scramble_mode:
            password = rotate_right(x, password)
        else:
            password = rotate_left(x, password)
    elif cmd == "rotate pos":
        if scramble_mode:
            password = rotate_pos(x, password)
        else:
            password = rotate_pos_reverse(x, password)
    elif cmd == "reverse positions":
        password = reverse_pos(x, y, password)
    elif cmd == "move position":
        if scramble_mode:
            password = move_pos(x, y, password)
        else:
            password = move_pos(y, x, password)

    return password


def process(commands, password):
    for command in commands:
        password = process_command(command, password, True)

    return password


def unscramble(commands, password):
    for command in commands[::-1]:
        password = process_command(command, password, False)

    return password


print(process(operations, "abcdefgh"))
print(unscramble(operations, "fbgdceah"))
