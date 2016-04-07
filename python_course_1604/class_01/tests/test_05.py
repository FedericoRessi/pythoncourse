'''
Created on 6 Apr 2016

@author: fressi
'''

import sys
import unittest

import mock

import python_course_1604.class_01.exercize_05_while_loop as exercize

from python_course_1604.tests.utils import skip_if_exercize_not_started


@skip_if_exercize_not_started(exercize)
class TestCaptureException(unittest.TestCase):

    def _mock_function(self, obj, name, *args, **kwargs):
        context = mock.patch.object(obj, name, *args, **kwargs)
        result = context.start()
        self.addCleanup(context.stop)
        return result

    def setUp(self):
        self._stdout = stdout = []
        self._mock_function(sys.stdout, 'write', side_effect=stdout.append)

    def test_has_something_to_do(self):
        assert exercize.has_something_to_do() is True

    def test_do_something(self):
        assert "some_result" == exercize.do_something()

    def test_when_no_loops(self):
        has_something_to_do = self._mock_function(
            exercize, 'has_something_to_do', return_value=False)

        do_something = self._mock_function(exercize, 'do_something')

        exercize.print_work_results()

        has_something_to_do.assert_called_once_with()
        do_something.assert_not_called()
        assert [] == self._stdout

    def test_when_some_loops(self):
        has_something_to_do = self._mock_function(
            exercize, 'has_something_to_do', side_effect=iter(
                [True, True, False]))

        do_something = self._mock_function(
            exercize, 'do_something', side_effect=iter(range(10)))

        exercize.print_work_results()

        has_something_to_do.assert_has_calls([mock.call()] * 3)
        do_something.assert_has_calls([mock.call()] * 2)
        assert ['0', '1'] == [s.strip() for s in self._stdout if s.strip()]
