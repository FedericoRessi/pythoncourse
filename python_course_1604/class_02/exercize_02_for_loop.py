'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''


def is_prime(number):
    """ It returns True if given number is prime."""

    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1

    return True


# Please modify below function to make it behaving as speicified in the
# function documentation.

def print_primes(max_number):
    """ Prints al prime numbers that are smaller than max_number

    To iterate numbers please use for statement with range function.
    To look if a number is prime it calls is_prime function.
    """
    for i in range(1, max_number):
        if is_prime(i):
            print(i)
