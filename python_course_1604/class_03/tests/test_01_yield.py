'''
Created on 25 Apr 2016

@author: fressi
'''

import unittest

import mock

import python_course_1604.class_03.exercize_01_yield as exercize

from python_course_1604.tests.utils import skip_if_exercize_not_started


@skip_if_exercize_not_started(exercize)
class TestYield(unittest.TestCase):

    def _mock_function(self, obj, name, *args, **kwargs):
        context = mock.patch.object(obj, name, *args, **kwargs)
        result = context.start()
        self.addCleanup(context.stop)
        return result

    def test_is_prime_with_1(self):
        result = exercize.is_prime(1)
        assert result is False

    def test_is_prime_with_2(self):
        result = exercize.is_prime(2)
        assert result is True

    def test_is_prime_with_4(self):
        result = exercize.is_prime(4)
        assert result is False

    def test_is_prime_with_7(self):
        result = exercize.is_prime(7)
        assert result is True

    def test_iter_primes_beteen_5_and_5(self):
        is_prime = self._mock_function(
            exercize, 'is_prime', side_effect=exercize.is_prime)

        primes = list(exercize.iter_prime_numbers(5, 5))

        assert [] == primes
        is_prime.assert_not_called()

    def test_iter_primes_beteen_0_and_2(self):
        is_prime = self._mock_function(
            exercize, 'is_prime', side_effect=exercize.is_prime)

        primes = list(exercize.iter_prime_numbers(0, 2))

        assert [] == primes
        is_prime.assert_has_calls([mock.call(i) for i in range(0, 2)])

    def test_iter_primes_beteen_0_and_10(self):
        is_prime = self._mock_function(
            exercize, 'is_prime', side_effect=exercize.is_prime)

        primes = list(exercize.iter_prime_numbers(0, 10))

        assert [2, 3, 5, 7] == primes
        is_prime.assert_has_calls([mock.call(i) for i in range(0, 10)])

    def test_iter_primes_beteen_3_and_6(self):
        is_prime = self._mock_function(
            exercize, 'is_prime', side_effect=exercize.is_prime)

        primes = list(exercize.iter_prime_numbers(3, 6))

        assert [3, 5] == primes
        is_prime.assert_has_calls([mock.call(i) for i in range(3, 6)])
