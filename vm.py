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

OP_EOP = "00"
OP_EOI = "01"
OP_PUSH = "02"
OP_POP = "03"
OP_PRINT = "04"
OP_ADD = "05"
OP_SUB = "06"


def load_program(argv):
    f = open(argv)
    lines = f.read().replace("\n", " ")
    lines = lines.split(" ")
    f.close()
    return lines


def execute_program(lines):
    print "program executed"


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
