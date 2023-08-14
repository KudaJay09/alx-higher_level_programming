#!/usr/bin/python3
# removes all characters c and C from a string.

def no_c(my_string):
<<<<<<< HEAD
    updated_str = ''
    for i in my_string:
        if i != 'c'and i != 'C':
            updated_str += i
            return (updated_str)
=======
    new_string = my_string.translate({ord(i): Non for i in 'cC'})

    return new_string
>>>>>>> 5f6dc0daac6fc7b2f191979753a1b3a623e5a055
