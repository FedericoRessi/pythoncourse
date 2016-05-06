'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''


def is_prime(number):
    """ It returns True if given number is prime."""

    # only numbers greater than 1 can be prime numbers
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            # the number is divisible by i
            return False

    return True


# Please modify below function to make it behaving as speicified in the
# function documentation.

def iter_prime_numbers(start, stop):
    """
    Generates an iterator over all prime numbers included between start
    (included) and stop (excluded)

    To look if a number is prime it calls is_prime function.
    To produce numbers please use yield statement
    """

    for number in range(start, stop):
        if is_prime(number):
            yield number
