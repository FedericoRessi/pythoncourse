'''
Created on 6 Apr 2016

@author: fressi
'''

import unittest

import python_course_1604.class_01.exercize_04_stack_limit as exercize

from python_course_1604.tests.utils import skip_if_exercize_not_started


@skip_if_exercize_not_started(exercize)
@unittest.skip('It brokes coverage.')
class TestStackLimit(unittest.TestCase):

    def test_failing_function(self):

        result = exercize.measure_stack_limit()

        expected_result = recursive_function(-2)
        assert result in range(expected_result - 5, expected_result + 5)


def recursive_function(level):
    try:
        return recursive_function(level + 1)
    except RuntimeError:
        return level
