import hashlib

dest = (3, 3)
states = [("njfxhljp", (0, 0))]

def is_open(code_char):
    return code_char > 'a'

def next_positions(position, str, code):
    if is_open(code[0]) and position[1] > 0:
        yield (str+'U', (position[0], position[1] - 1))
    if is_open(code[1]) and position[1] < 3:
        yield (str+'D', (position[0], position[1] + 1))
    if is_open(code[2]) and position[0] > 0:
        yield (str+'L', (position[0] - 1, position[1]))
    if is_open(code[3]) and position[0] < 3:
        yield (str+'R', (position[0] + 1, position[1]))

def run():
    while len(states) != 0:
        state = states[0]
        states.remove(state)
        input = state[0]
        pos = state[1]
        code = hashlib.md5(str.encode(input)).hexdigest()[:4]

        for new_state in next_positions(pos, input, code):
            new_input = new_state[0]
            new_pos = new_state[1]
            if new_pos == dest:
                #return new_input
                print(len(new_input) - 8)
            else:
                states.append(new_state)

run()
