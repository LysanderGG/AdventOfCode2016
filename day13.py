FAV_NUMBER = 1350


def is_open_space(x, y):
    calc = x*x + 3*x + 2*x*y + y + y*y + FAV_NUMBER
    return bin(calc).count('1') % 2 == 0


def next_coord(x, y):
    next_coords = []
    if x > 0:
        next_coords.append((x - 1, y))
    if y > 0:
        next_coords.append((x, y - 1))
    next_coords.append((x + 1, y))
    next_coords.append((x, y + 1))

    return [(x, y) for (x, y) in next_coords if is_open_space(x, y)]


def explore_maze(start, goal):
    # The maze is the following data structure: 
    #   [{start}, {coords reachable with 1 step}, {coords reachable with 2 steps}, ...]
    # Further levels do not contain coordinates found at previous levels
    maze = [{start}] 
    stop = False

    while not stop:
        last_level = maze[-1]
        next_level = set()

        for last_coord in last_level:
            for c in next_coord(last_coord[0], last_coord[1]):
                if goal == c:
                    stop = True
                
                if c not in [elem for level in maze for elem in level]:
                    next_level.add(c)
        maze.append(next_level)

    return maze


if __name__ == "__main__":
    start = (1,1)
    goal = (31,39)

    maze = explore_maze(start, goal)

    ans = len(maze) - 1
    print("Part1: {}".format(ans))

    ans2 = sum(len(level) for level in maze[:51])
    print("Part2: {}".format(ans2))
