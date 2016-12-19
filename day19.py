input = 3005290

l = [(i,1) for i in range(1, input+1)]
i = 0


def remove_zeros(l):
    return [e for e in l if e[1] != 0]

while len(l) > 1:
    i_next = i+1 if i+1 < len(l) else 0
    l[i] = (l[i][0], l[i][1] + l[i_next][1])
    l[i_next] = (l[i_next][0], 0)
    
    i += 2
    if i >= len(l):
        print(len(l))
        l = remove_zeros(l)
        i = 0

print(l)