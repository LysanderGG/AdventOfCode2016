input = 3005290

def remove_zeros(l):
    return [e for e in l if e[1] != 0]


def elves_play_1(nb_elves):
    i = 0
    l = [(i,1) for i in range(1, nb_elves+1)]
    while len(l) > 1:
        i_next = i+1 if i+1 < len(l) else 0
        l[i] = (l[i][0], l[i][1] + l[i_next][1])
        l[i_next] = (l[i_next][0], 0)
    
        i += 2
        if i >= len(l):
            l = remove_zeros(l)
            i = 0

    return l[0][0]


# Part 2 would have been way simpler and cleaner with linked list
# but hey why make it simple when you can make it complicated

def next_idx(l, i):
    i_next = i+1 
    if i_next >= len(l):
       i_next = 0

    while i_next < len(l) and l[i_next][1] == 0:
        i_next += 1
    if i_next == len(l):
        return 0

    return i_next


def opposite_idx(l, i, nb_removed):
    return (i + (len(l) + nb_removed) // 2) % len(l)


def remove_zeros_and_keep_current(l, i_current):
    current_elem = l[i_current]
    l = remove_zeros(l)
    return l, l.index(current_elem)

def elves_play_2(nb_elves):
    i = 0
    first_half = True
    nb_removed = 0
    l = [(i,1) for i in range(1, nb_elves+1)]
    while len(l) > 1:
        if (first_half and i >= len(l) // 2) \
        or (not first_half and i <= len(l) // 2):
            first_half = not first_half
            nb_removed = 0
            l, i = remove_zeros_and_keep_current(l, i)
        elif len(l) < 3:
            nb_removed = 0
            l, i = remove_zeros_and_keep_current(l, i)
            continue

        i_opp = opposite_idx(l, i, nb_removed)
        l[i] = (l[i][0], l[i][1] + l[i_opp][1])
        l[i_opp] = (l[i_opp][0], 0)
        nb_removed += 1

        i = next_idx(l, i)

    return l[0][0]


print("Part1: ", elves_play_1(input))
print("Part2: ", elves_play_2(input))
