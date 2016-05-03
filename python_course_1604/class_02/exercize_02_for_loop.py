'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''


def is_prime(number):
    """ returns True if given number is prime
    """
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1

    return True


def print_primes(max_number):
    """ Prints al prime numbers that are smaller than max_number

    To iterate numbers please use for statement with range function.
    To look if a number is prime it calls is_prime function.
    """
    for num in range(1, max_number, 1):
        if is_prime(num):
            print(num)
