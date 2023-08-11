#!/usr/bin/python3
# prints the result of the addition of all arguments

if __name__ == " __main__ ":
    from sys import argv
    argument_sum = 0
    number_of_arguments = len(argv)

    for i in range(1, number_of_arguments):
        argument_sum += int(argv[i])

        print(argument_sum)
