'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Complete count_until function to sarisfy documented behaviour


def has_next():
    """Function that return True when there is still something to do and False
    in all other cases.
    """

    return True


def get_next():
    """Function that do something.
    """
    return "some_value"


def count_until(match_value):
    """Function looks if a value is contained on a list of values.

    Every loop the function takes a new value calling get_next()

    It lools until one of following happens:
        - has_next returns True
        - get_next() returns a value equal to match_value

    It returns the number of times it calls get_next().
    It raises KeyError when has_next() returns False before searched value is
    found.

    Please use while, break, else construct.
    """
    loops = 0

    while has_next():
        loops += 1
        if get_next() == match_value:
            break
    
    else:
        raise KeyError


    return loops
    
