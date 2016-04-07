'''
Created on 6 Apr 2016

@author: fressi
'''

import unittest

import mock

import python_course_1604.class_01.exercize_06_while_break_else as exercize

from python_course_1604.tests.utils import skip_if_exercize_not_started


@skip_if_exercize_not_started(exercize)
class TestCaptureException(unittest.TestCase):

    def _mock_function(self, obj, name, *args, **kwargs):
        context = mock.patch.object(obj, name, *args, **kwargs)
        result = context.start()
        self.addCleanup(context.stop)
        return result

    def test_has_next(self):
        assert exercize.has_next() is True

    def test_get_next(self):
        assert "some_value" == exercize.get_next()

    def test_when_no_loops(self):
        has_next = self._mock_function(
            exercize, 'has_next', return_value=False)

        get_next = self._mock_function(exercize, 'get_next')

        with self.assertRaises(KeyError):
            exercize.count_until(7)

        has_next.assert_called_once_with()
        get_next.assert_not_called()

    def test_when_has_next_give_false_before_searched_value(self):
        has_next = self._mock_function(
            exercize, 'has_next', side_effect=iter(
                [True, True, False]))

        get_next = self._mock_function(
            exercize, 'get_next', side_effect=iter(range(10)))

        with self.assertRaises(KeyError):
            exercize.count_until(7)

        has_next.assert_has_calls([mock.call()] * 3)
        get_next.assert_has_calls([mock.call()] * 2)

    def test_when_has_next_give_false_after_searched_value(self):
        has_next = self._mock_function(
            exercize, 'has_next', side_effect=iter(
                [True] * 10 + [False]))

        get_next = self._mock_function(
            exercize, 'get_next', side_effect=iter(range(10)))

        result = exercize.count_until(7)

        assert 8 == result
        has_next.assert_has_calls([mock.call()] * 8)
        get_next.assert_has_calls([mock.call()] * 7)
