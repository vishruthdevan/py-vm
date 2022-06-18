def main(argv):
    print "hello world"
    return 0


def target(*args):
    return main, None


if __name__ == "__main__":
    main(sys.argv)
