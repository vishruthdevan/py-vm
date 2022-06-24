import sys

'''
Instructions:

00 - End of the program
01 - End of the instruction
02 - Push
03 - Pop
04 - Print
05 - Add
06 - Subtract

'''

stack = []

OP_EOP = "00"
OP_EOI = "01"
OP_PUSH = "02"
OP_POP = "03"
OP_PRINT = "04"
OP_ADD = "05"
OP_SUB = "06"


def do_eoi():
    pass


def do_push(i, l):
    stack.append(int(l[i+1], 16))


def do_pop():
    stack.pop()


def do_print():
    print stack[-1]


def do_add():
    s = stack[-1] + stack[-2]
    stack.pop()
    stack.pop()
    stack.append(s)


def do_sub():
    s = stack[-1] - stack[-2]
    stack.pop()
    stack.pop()
    stack.append(s)


def load_program(argv):
    f = open(argv)
    lines = f.read().replace("\n", " ")
    lines = lines.split(" ")
    f.close()
    return lines


def execute_program(l):
    loop = 1
    i = 0
    while loop == 1:
        instruction = l[i]
        if instruction == OP_EOP:
            loop = 0
        elif instruction == OP_PUSH:
            do_push(i, l)
        elif instruction == OP_POP:
            do_pop()
        elif instruction == OP_PRINT:
            do_print()
        elif instruction == OP_ADD:
            do_add()
        elif instruction == OP_SUB:
            do_sub()
        i += 1


def run_program(argv):
    lines = load_program(argv)
    execute_program(lines)


def main(argv):
    run_program(argv[1])
    return 0


def target(*args):
    return main, None


if __name__ == "__main__":
    main(sys.argv)
