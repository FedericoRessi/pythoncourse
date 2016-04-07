'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Complete recursive_func function to sarisfy documented behaviour


def measure_stack_limit():
    """Function that measures actual stack limit.

    This function calls a new recoursive function to reach stack limit and
    counts the number of calls.

    It returns the number of recoursive functions calls before stack limit is
    reached.
    """

    return recursive_function(0)


def recursive_function(level):
    """Function that recursively calls himseld with level + 1 as parameter

    It returns level when stack limit is reached.
    It returns the result of recursive call if limit is not reached.

    Hints: when stack limit is reached RuntimeError is raised.
    """

    try:
        return recursive_function(level)
    except RuntimeError:
        return level
