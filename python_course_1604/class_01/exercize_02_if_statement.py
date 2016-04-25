'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Complete clamp function to sarisfy documented behaviour


def clamp(value, min_value, max_value):

    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value
