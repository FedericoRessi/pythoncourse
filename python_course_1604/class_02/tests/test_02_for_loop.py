'''
Created on 25 Apr 2016

@author: fressi
'''

import sys
import unittest

import mock

import python_course_1604.class_02.exercize_02_for_loop as exercize

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

    def test_is_prime_with_1(self):
        result = exercize.is_prime(1)
        assert result is True

    def test_is_prime_with_4(self):
        result = exercize.is_prime(4)
        assert result is False

    def test_is_prime_with_7(self):
        result = exercize.is_prime(7)
        assert result is True

    def test_print_primes_with_1(self):
        is_prime = self._mock_function(
            exercize, 'is_prime', side_effect=exercize.is_prime)

        exercize.print_primes(1)

        is_prime.assert_not_called()
        assert [] == [s.strip() for s in self._stdout if s.strip()]

    def test_with_5(self):
        is_prime = self._mock_function(
            exercize, 'is_prime', side_effect=exercize.is_prime)

        exercize.print_primes(5)

        is_prime.assert_has_calls([mock.call(i) for i in range(1, 5)])
        assert ['1', '2', '3'] == [
            s.strip() for s in self._stdout if s.strip()]

    def test_with_10(self):
        is_prime = self._mock_function(
            exercize, 'is_prime', side_effect=exercize.is_prime)

        exercize.print_primes(10)

        is_prime.assert_has_calls([mock.call(i) for i in range(1, 10)])
        assert ['1', '2', '3', '5', '7'] == [
            s.strip() for s in self._stdout if s.strip()]
