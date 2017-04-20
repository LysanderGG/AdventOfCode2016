import re


def read_input(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f]


def split_line(line):
    parts = line.split(" ")
    if len(parts) == 2:
        return (parts[0], parts[1], None)
    else:
        return parts


def process(instructions, registers):
    pc = 0
    while pc < len(instructions):
        instr, op1, op2 = split_line(instructions[pc])
        if instr == "cpy":
            registers[op2] = registers[op1] if op1.isalpha() else int(op1)
        elif instr == "jnz":
            val = registers[op1] if op1.isalpha() else int(op1)
            if val != 0:
                pc += int(op2)
                continue
        elif instr == "inc":
            registers[op1] += 1
        elif instr == "dec":
            registers[op1] -= 1

        pc += 1


if __name__ == "__main__":
    instructions = read_input("day12.txt")
    
    registers1 = {"a":0, "b":0, "c":0, "d":0}
    process(instructions, registers1)
    print("Part1: value in a is {}".format(registers1["a"]))

    registers2 = {"a":0, "b":0, "c":1, "d":0}
    process(instructions, registers2)
    print("Part1: value in a is {}".format(registers2["a"]))
