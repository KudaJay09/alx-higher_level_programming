#!/usr/bin/python3
# prints the ASCII alphabet, in lowercase

for j in range(97, 123):
    if j != 101 and j != 113:
        print("{}".format(chr(j)), end="")
