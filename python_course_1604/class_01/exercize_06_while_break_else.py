'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Complete count_until function to sarisfy documented behaviour


def has_next():
    """ Function that returns:
        - True when there is still something to do
        - False in all other cases.
    """

    return True


def get_next():
    """ Function that does something and that returns some value.
    """

    return "some_value"


def count_until(match_value):
    """Function looks if a value is contained in a sequence of values.

    It loops until one of following happens:
        - has_next returns True
        - get_next() returns a value equal to match_value

    In every loop the function takes a new value calling get_next()

    It returns the number of times it calls get_next().
    It raises KeyError when has_next() returns False before searched value is
    found.

    Please use while-break-else construct.
    """
