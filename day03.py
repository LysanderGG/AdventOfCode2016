import sys


def read_triangles_horizontal(filepath):
    triangles = []
    with open(filepath) as f:
        for line in f:
            triangles.append([int(x) for x in line.split()])

    return triangles


def read_triangles_vertical(filepath):
    triangles = []
    i_line = 0
    i_tri = -3
    with open(filepath) as f:
        for line in f:
            if i_line % 3 == 0:
                triangles.append([])
                triangles.append([])
                triangles.append([])
                i_tri += 3
            vals = [int(x) for x in line.split()]
            for i in range(0, 3):
                triangles[i_tri + i].append(vals[i])

            i_line += 1

    return triangles


def get_nb_valid_triangles(triangles):
    n = 0
    for t in triangles:
        if  t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[2] + t[0] > t[1]:
            n += 1
    return n


print("Part 1:", get_nb_valid_triangles(read_triangles_horizontal("day03.txt")))
print("Part 2:", get_nb_valid_triangles(read_triangles_vertical("day03.txt")))
