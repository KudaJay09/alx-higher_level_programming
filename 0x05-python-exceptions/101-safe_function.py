#!/usr/bin/python3
# executes a function safely.
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return (None)
