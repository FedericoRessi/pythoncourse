'''
Created on 6 Apr 2016

@author: fressi
'''
import unittest


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        from python_course_1604.class_01.exercize_02_if_statement import clamp
        self.clamp = clamp

    def test_when_x_is_smaller_than_min_value(self):
        assert 10 == self.clamp(-10, 10, 20)

    def test_when_x_is_greater_than_max_value(self):
        assert 20 == self.clamp(50, 10, 20)

    def test_when_x_is_between_min_value_and_max_value(self):
        assert 15 == self.clamp(15, 10, 20)
