#!/usr/bin/python3
# prints the result of the addition of all arguments

if __name__ == "__main__":
    import sys
    argument_sum = 0

    for i in range(len(sys.argv) - 1):
        argument_sum += int(sys.argv[i + 1])

        print("{}".format(argument_sum))
