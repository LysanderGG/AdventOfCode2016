import sys


def is_wall(floor_map, pos):
    return floor_map[pos[1]][pos[0]] == '#'


def checkpoint_value(floor_map, pos):
    try: 
        checkpoint = int(floor_map[pos[1]][pos[0]])
        return checkpoint
    except ValueError:
        return -1


def list_checkpoints(floor_map):
    checkpoints = []
    for y in range(len(floor_map)):
        line = floor_map[y]
        for x in range(len(line)):
            checkpoint = checkpoint_value(floor_map, (x, y))
            if checkpoint > 0:
                checkpoints.append(checkpoint)
    return checkpoints


def start_position(floor_map):
    for y in range(len(floor_map)):
        line = floor_map[y]
        if '0' in line:
            x = line.index('0')
            return (x, y)
    assert(0)


def next_pos(floor_map, curr_pos):
    pos = []
    width = len(floor_map[0])
    height = len(floor_map)
    x, y = curr_pos 
    if x > 0 and not is_wall(floor_map, (x - 1, y)):
        pos.append((x - 1, y))
    if x < width - 1 and not is_wall(floor_map, (x + 1, y)):
        pos.append((x + 1, y))
    if y > 0 and not is_wall(floor_map, (x, y - 1)):
        pos.append((x, y - 1))
    if y < height - 1 and not is_wall(floor_map, (x, y + 1)):
        pos.append((x, y + 1))

    return pos


# Return (nb_it_all_checkpoints, nb_it_return, list of new states)
# return values 0 and 1 can be 0 meaning the goal has not been reached.
def step(floor_map, state):
    ret_nb_it = 0
    curr_pos, nb_it, checkpoints = state
    c = checkpoint_value(floor_map, curr_pos)
    if c >= 0 and c in checkpoints:
        checkpoints = [a for a in checkpoints if a != c]
        if len(checkpoints) == 0:
            if c != 0:
                ret_nb_it = nb_it
                print("Reached end in", nb_it)
                checkpoints.append(0)
            else: 
                print("Reached 0 in", nb_it)
                return 0, nb_it, []

    next_positions = next_pos(floor_map, curr_pos)
    next_states = []
    for pos in next_positions:
        next_states.append((pos, nb_it + 1, checkpoints))

    return ret_nb_it, 0, next_states


# Return False if the state is already in the history 
# or a better state is already in the history
def check_against_history(history, state):
    pos, nb_it, checkpoints = state
    for hist_state in history:
        if pos == hist_state[0] and checkpoints == hist_state[2]:
            return nb_it < hist_state[1]
    return True


def load_map(path):
    floor_map = []
    with open(path) as f:
        for line in f:
            s = [a for a in line]
            floor_map.append(s[:len(s)-1])
    
    # remove first and last lines are they are just walls
    return floor_map[1:len(floor_map)-1]


def solve(path):
    floor_map = load_map(path)
    checkpoints = list_checkpoints(floor_map)
    start_pos = start_position(floor_map)
    #state: (position, nb_moves, remaining_checkpoints)
    states = [(start_pos, 0, checkpoints)]
    history = [states[0]]

    i = 0
    nb_it_all_checkpoints = 0
    while len(states) > 0:
        i += 1
        state = states.pop(0)
        a, nb_it_return, new_states = step(floor_map, state)
        if a > 0 and nb_it_all_checkpoints == 0:
            nb_it_all_checkpoints = a
        if nb_it_all_checkpoints > 0 and nb_it_return > 0:
            break

        for new_state in new_states:
            if check_against_history(history, new_state):
                states.append(new_state)
                history.append(new_state)

        if i % 1000 == 0:
            nb_min_states = len(state[2])
            for s in states:
                nb_min_states = min(nb_min_states, len(s[2]))
            
            states = [s for s in states if len(s[2]) <= (nb_min_states + 1)]
            print(len(states), len(history), nb_min_states)

    return nb_it_all_checkpoints, nb_it_return


#print(solve("day24-example.txt"))
print(solve("day24.txt"))
