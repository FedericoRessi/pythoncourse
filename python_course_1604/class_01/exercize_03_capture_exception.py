'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Complete failing_function and capute_exception function to sarisfy documented
# behaviour


def failing_function():
    """Function thar raises a RuntimeError
    """
    raise RuntimeError


def capute_exception():
    """Function that calls failing_function and caputes RuntimeError exception

    It returns:
        True when no exceptions are raised by failing_function.
        False when RuntimeException is raised by failing_function.

    If any else exception is raised, then it must let it pass on.
    Please use try: except: else: construct.
    """
    try:
        failing_function()
    except RuntimeError:
        return False
    except:
        raise
    else:
        return True
