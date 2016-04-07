'''
Created on 6 Apr 2016

@author: fressi
'''

import unittest

import python_course_1604.class_01.exercize_04_stack_limit as exercize


class TestStackLimit(unittest.TestCase):

    def test_failing_function(self):

        result = exercize.measure_stack_limit()

        assert recursive_function(-1) == result


def recursive_function(level):
    try:
        return recursive_function(level + 1)
    except RuntimeError:
        return level
