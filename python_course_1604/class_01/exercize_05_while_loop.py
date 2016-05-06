'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Complete print_work_results function to sarisfy documented behaviour


def has_something_to_do():
    """Function that return True when there is still something to do and False
    in all other cases.
    """

    return True


def do_something():
    """Function that do something.
    """
    return "some_result"


def print_work_results():
    """Function that loops until has_something_to_do() returns True
    calling do_something() function and printing its results.

    Please use while construct.
    """
    while has_something_to_do():
        print (do_something())
