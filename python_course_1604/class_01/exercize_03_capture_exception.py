'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Complete failing_function and capute_exception function to sarisfy documented
# behaviour


def failing_function():

    raise RuntimeError    # Raise a RuntimeError


def capute_exception():

    try:
        failing_function()
    except RuntimeError:
        return False
    else:
        return True
