'''
Created on 25 Apr 2016

@author: fressi
'''

import sys
import unittest

import mock

import python_course_1604.class_02.exercize_03_break_and_continue as exercize

from python_course_1604.tests.utils import skip_if_exercize_not_started


@skip_if_exercize_not_started(exercize)
class TestForLoop(unittest.TestCase):

    def _mock_function(self, obj, name, *args, **kwargs):
        context = mock.patch.object(obj, name, *args, **kwargs)
        result = context.start()
        self.addCleanup(context.stop)
        return result

    def setUp(self):
        self._stdout = stdout = []
        self._mock_function(sys.stdout, 'write', side_effect=stdout.append)

    def test_print_pong(self):
        exercize.execute_commands(['ping'])

        assert ['pong'] == [
            s.strip() for s in self._stdout if s.strip()]

    def test_print_unknown_command(self):
        exercize.execute_commands(['do-all'])

        assert ['error'] == [
            s.strip() for s in self._stdout if s.strip()]

    def test_quit_command_after_1_ping(self):
        exercize.execute_commands(['ping', 'quit', 'ping'])

        assert ['pong'] == [
            s.strip() for s in self._stdout if s.strip()]

    def test_quit_command_after_2_pings(self):
        exercize.execute_commands(['ping', 'ping', 'quit', 'ping'])

        assert ['pong', 'pong'] == [
            s.strip() for s in self._stdout if s.strip()]

    def test_skip_command(self):
        exercize.execute_commands(['skip', 'quit', 'ping'])

        assert ['pong'] == [
            s.strip() for s in self._stdout if s.strip()]
