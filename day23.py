import re


def read_input(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f]


def split_line(line):
    parts = line.split(" ")
    if len(parts) == 1:
        return (parts[0], None, None)
    elif len(parts) == 2:
        return (parts[0], parts[1], None)
    else:
        return parts


def eval_arg(registers, op):
    return registers[op] if op.isalpha() else int(op)


def tgl_line(line):
    parts = line.split(" ")
    if len(parts) == 2:
        newInstr = "dec" if parts[0] == "inc" else "inc"
        return newInstr + line[3:]
    else:
        newInstr = "cpy" if parts[0] == "jnz" else "jnz"
        return newInstr + line[3:]


def process(instructions, registers):
    pc = 0
    while pc < len(instructions):
        instr, op1, op2 = split_line(instructions[pc])
        if instr == "cpy":
            if op2 in registers:
                registers[op2] = eval_arg(registers, op1)
        elif instr == "jnz":
            if eval_arg(registers, op1) != 0:
                pc += eval_arg(registers, op2)
                continue
        elif instr == "inc":
            registers[op1] += 1
        elif instr == "dec":
            registers[op1] -= 1
        elif instr == "tgl":
            val = pc + eval_arg(registers, op1)
            if 0 <= val < len(instructions):
                instructions[val] = tgl_line(instructions[val])
        elif instr == "add":
            if op2 in registers:
                registers[op2] += eval_arg(registers, op1)
        elif instr == "mul":
            if op2 in registers:
                registers[op2] *= eval_arg(registers, op1)

        pc += 1


if __name__ == "__main__":
    instructions = read_input("day23.txt")
    
    registers1 = {"a":7, "b":0, "c":0, "d":0}
    process(instructions, registers1)
    print("Part1: value in a is {}".format(registers1["a"]))
    
    instructions = read_input("day23-mul.txt")

    registers2 = {"a":12, "b":0, "c":0, "d":0}
    process(instructions, registers2)
    print("Part2: value in a is {}".format(registers2["a"]))
