#!/usr/bin/python3
# creates new copy of a string and removes character at position 'n'

i = 0
for p in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(p - i)), end="")
    i = 32 if i == 0 else 0
