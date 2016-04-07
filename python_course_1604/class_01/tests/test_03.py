'''
Created on 6 Apr 2016

@author: fressi
'''

import unittest
import mock

import python_course_1604.class_01.exercize_03_capture_exception as exercize


class TestCaptureException(unittest.TestCase):

    def _mock_function(self, obj, name, *args, **kwargs):
        context = mock.patch.object(obj, name, *args, **kwargs)
        result = context.start()
        self.addCleanup(context.stop)
        return result

    def test_failing_function(self):
        with self.assertRaises(RuntimeError):
            exercize.failing_function()

    def test_when_no_exception_is_raised(self):

        mocked_failing_function = self._mock_function(
            exercize, 'failing_function', return_value=None)

        result = exercize.capute_exception()

        assert result is True
        mocked_failing_function.assert_called_once_with()

    def test_when_runtime_error_is_raised(self):

        mocked_failing_function = self._mock_function(
            exercize, 'failing_function', side_effect=RuntimeError)

        result = exercize.capute_exception()

        assert result is False
        mocked_failing_function.assert_called_once_with()

    def test_when_other_exception_is_raised(self):

        mocked_failing_function = self._mock_function(
            exercize, 'failing_function', side_effect=ValueError)

        with self.assertRaises(ValueError):
            exercize.capute_exception()

        mocked_failing_function.assert_called_once_with()
