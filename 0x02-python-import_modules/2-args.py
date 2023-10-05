#!/usr/bin/python3
import sys
def main():
    num_args = len(sys.argv)
    print("Number of arguments is: {}".format(num_args - 1))

    print("List of arguments:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("Argument {}: {}".format(i, arg))

if __name__ == "__main__":
    main()
