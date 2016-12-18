def is_trap(char):
    return char == '^'


def new_tile(row, idx):
    left = row[idx - 1] if idx > 0  else "."
    right = row[idx + 1] if idx < len(row) - 1  else "."
    if (is_trap(left) and not is_trap(right)) or (not is_trap(left) and is_trap(right)):
        return "^"
    return "."


def get_next_row(row):
    next_row = []
    for i in range(len(row)):
        next_row.append(new_tile(row, i))
    return next_row


def count_safe(row):
    return row.count(".")


def solve(first_row, total_rows):
    row = first_row
    nb_rows = 0
    nb_safe = 0
    while nb_rows < total_rows:
        nb_safe += count_safe(row)
        nb_rows += 1
        row = get_next_row(row)

    return nb_safe


input_row = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^"
print("18.a: ", solve(input_row, 40))
print("18.b: ", solve(input_row, 400000))
