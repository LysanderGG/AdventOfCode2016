import itertools

f0 = ( (0, # elevator floor
        (frozenset(('m1', 'm2')),   # first floor
         frozenset(('g1',)),        # 2nd floor
         frozenset(('g2',)),        # 3rd floor
         frozenset(()))
        ),
      )

f0_target = (3,
             (frozenset(()),
              frozenset(()),
              frozenset(()),
              frozenset(('m1', 'm2', 'g1', 'g2'))
              )
             )

f1 = ( (0,
        (frozenset(('g1', 'm1', 'g2', 'm2')),
         frozenset(('g3', 'm4', 'g4', 'm5', 'g5')),
         frozenset(('m3',)),
         frozenset(()))
         ),
    )

f1_target = (3,
             (frozenset(()),
              frozenset(()),
              frozenset(()),
              frozenset(('m1', 'm2', 'm3', 'm4', 'm5', 'g1', 'g2', 'g3', 'g4', 'g5'))
              )
             )

f2 = ( (0,
        (frozenset(('g1', 'm1', 'g2', 'm2', 'm6', 'm7', 'g6', 'g7')),
         frozenset(('g3', 'm4', 'g4', 'm5', 'g5')),
         frozenset(('m3',)),
         frozenset(()))
         ),
    )

f2_target = (3,
             (frozenset(()),
              frozenset(()),
              frozenset(()),
              frozenset(('m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7'))
              )
             )

# state: list of frozensets
# i_to_test: list of floor indices to test for validity
def is_valid_state(state, i_to_test):
    for i in i_to_test:
        floor = state[i]
        power_arr = [e[0] == 'g' or e[0] == 'm' and 'g' + str(e[1]) in floor for e in floor]
        if all(power_arr) or not any(power_arr): continue
        
        for power, elem in zip(power_arr, floor):
            if power == False and 'm' == elem[0]:
                return False
    return True


# Add new_outcome to possible_outcomes if new_outcome[0] and i_prev are valids
# and not already in levels.
# possible_outcomes: list of possible outcomes (elevator floor, (floors))
# new_outcome: (elevator floor, (floors))
# i_prev: int
# levels: dictionnary
# i_level: current level in the graph
def add_possible_outcome(possible_outcomes, new_outcome, i_prev, levels, i_level):
    if new_outcome not in levels and is_valid_state(new_outcome[1], (i_prev, new_outcome[0])):
        levels[new_outcome] = i_level
        possible_outcomes.append(new_outcome)


# outcome: list of frozensets
# elems_to_remove: list of elements to remove
def new_outcome_remove(outcome, elems_to_remove):
    a = list(outcome)
    for elem in elems_to_remove:
        a.remove(elem)
    return frozenset(a)


# outcome: list of frozensets
# elems_to_append: list of elements to append
def new_outcome_append(outcome, elems_to_append):
    a = list(outcome)
    for elem in elems_to_append:
        a.append(elem)
    return frozenset(a)


# Notes:
#  - There is no point in bringing 2 items down.
def possible_steps(state, levels, i_level):
    possible_outcomes = []
    i_floor, state = state

    if i_floor < 3:
        for elem in state[i_floor]:
            new_outcome = list(state)
            new_outcome[i_floor] = new_outcome_remove(new_outcome[i_floor], [elem])
            new_outcome[i_floor+1] = new_outcome_append(new_outcome[i_floor+1], [elem])
            add_possible_outcome(possible_outcomes, (i_floor+1, tuple(new_outcome)), i_floor, levels, i_level)
        for combi in itertools.combinations(state[i_floor], 2):
            new_outcome = list(state)
            new_outcome[i_floor] = new_outcome_remove(new_outcome[i_floor], combi)
            new_outcome[i_floor+1] = new_outcome_append(new_outcome[i_floor+1], combi)
            add_possible_outcome(possible_outcomes, (i_floor+1, tuple(new_outcome)), i_floor, levels, i_level)
    if i_floor > 0:
        for elem in state[i_floor]:
            new_outcome = list(state)
            new_outcome[i_floor] = new_outcome_remove(new_outcome[i_floor], [elem])
            new_outcome[i_floor-1] = new_outcome_append(new_outcome[i_floor-1], [elem])
            add_possible_outcome(possible_outcomes, (i_floor-1, tuple(new_outcome)), i_floor, levels, i_level)

    return possible_outcomes


def solve(start_state, target_state):
    levels = {start_state[0][1]: 0}
    i = 1
    states = list(start_state);

    while states and target_state not in states:
        next = []
        for state in states:
            for next_state in possible_steps(state, levels, i):
                next.append(next_state)
        states = next
        print("level {}: {} elements".format(i, len(levels)))
        i += 1
    return levels[target_state]

import time
if __name__ == "__main__":
    #ans = solve(f0, f0_target)
    #print(ans)

    ans = solve(f1, f1_target)
    print("Part1: {}".format(ans))

    start_time = time.time()
    ans = solve(f2, f2_target)
    print("--- %s seconds ---" % (time.time() - start_time))

    print("Part2: {}".format(ans))
