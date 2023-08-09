#!/usr/bin/python3
# create a new string copy with no character at 'n'

def remove_char_at(str, n):
    if n < 0:
        return(str)
    return(str[:n] + str[n+1:])
