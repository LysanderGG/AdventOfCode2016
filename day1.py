input = "L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2"

x = 0
y = 0
curr_dir = 0 # 0: North, 1: East, ...
visited_pos = [(0,0)]

def add_history(val):
    if val in visited_pos: 
        print(val, abs(val[0]) + abs(val[1]))
    visited_pos.append(val)

input_cmd = input.split(", ")
for step in input_cmd:
    dir = step[0]
    len = int(step[1:])

    if   dir == "L": curr_dir = (curr_dir + 4 - 1) % 4
    elif dir == "R": curr_dir = (curr_dir + 1) % 4
    
    x_step = 0
    y_step = 0
    if   curr_dir == 0: y_step = len
    elif curr_dir == 1: x_step = len
    elif curr_dir == 2: y_step = -len
    elif curr_dir == 3: x_step = -len

    if abs(x_step) > 0:
        step_unit = x_step//abs(x_step)
        for _x in range(step_unit, x_step + step_unit, step_unit):
            x += step_unit
            add_history((x, y))

    if abs(y_step) > 0:
        step_unit = y_step//abs(y_step)
        for _y in range(step_unit, y_step + step_unit, step_unit):
            y += step_unit
            add_history((x, y))

total_distance = abs(x) + abs(y)
print(total_distance)
