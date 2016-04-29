'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Complete clamp function to satisfy documented behaviour


def clamp(value, min_value, max_value):
    """Function that:

    - Returns min_value when value is smaller than min_value
    - Returns max_value when value is greater than max_value
    - Returns value in all other cases

    Please use if, elif and else keywords
    """

    if(value < min_value):
        return min_value
    if(value > max_value):
        return max_value
    return value

print (clamp(3, 4, 5))
