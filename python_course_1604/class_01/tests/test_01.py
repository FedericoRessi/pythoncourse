'''
Created on 6 Apr 2016

@author: fressi
'''
import unittest


class TestHelloWorld(unittest.TestCase):

    def test_hello_world_exists(self):
        from sh import python
        output = python(
            '-m', 'python_course_1604.class_01.exercize_01_hello_world')
        assert 'Hello world!\n' == output,\
            "Write a line that prints 'Hello world!'"
