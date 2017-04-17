import numpy as np
import re


def read_input(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f]


def process_instruction(instruction, pixels):
    rect = re.match("rect (\d+)x(\d+)", instruction)
    col = re.match("rotate column x=(\d+) by (\d+)", instruction)
    row = re.match("rotate row y=(\d+) by (\d+)", instruction)
    if rect:
        w = int(rect.group(1))
        h = int(rect.group(2))
        pixels[0:h,0:w] = 1.0
    elif col:
        y = int(col.group(1))
        n = int(col.group(2))
        pixels[:,y] = np.roll(pixels[:,y], n)
    elif row:
        x = int(row.group(1))
        n = int(row.group(2))
        pixels[x] = np.roll(pixels[x], n)

    return pixels

def process_instructions(instructions, pixels):
    for instruction in instructions:
        pixels = process_instruction(instruction, pixels)
    return pixels


if __name__ == "__main__":
    instructions = read_input("day08.txt")
    pixels = np.zeros((6, 50))
    
    pixels = process_instructions(instructions, pixels)
    ans = np.sum(pixels)
    print("Part1: {}".format(ans))

    print("Part2: \n {}".format(pixels))
