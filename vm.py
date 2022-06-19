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

def load_program(argv):
    print "program loaded"

def execute_program():
    print "program executed"

def run_program(argv):
    load_program(argv)
    execute_program()

def main(argv):
    run_program(argv[1])
    return 0

def target(*args):
    return main, None

if __name__ == "__main__":
    main(sys.argv)
