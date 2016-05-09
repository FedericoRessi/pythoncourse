'''
Created on 9 May 2016

@author: fressi
'''

import unittest

import mock

import python_course_1604.class_03.exercize_02_finally as exercize

from python_course_1604.tests.utils import skip_if_exercize_not_started


@skip_if_exercize_not_started(exercize)
class TestFinally(unittest.TestCase):

    def test_start_transaction(self):
        result = exercize.start_transaction()

        assert isinstance(result, int)
        assert result >= 1
        assert result < 1000

    def test_execute_transaction_operation(self):
        exercize.execute_transaction_operation(125, 'some_operation')

    def test_close_transaction(self):
        exercize.close_transaction(125)

    def test_try_transaction_0_times(self):
        start = self._mock_start()
        execute = self._mock_execute()
        close = self._mock_close()

        result =\
            exercize.try_execute_transaction_operations([1, 2, 3], 0)

        assert result is False

        start.assert_not_called()
        execute.assert_not_called()
        close.assert_not_called()

    def test_try_transaction_1_time(self):
        start = self._mock_start()
        execute = self._mock_execute()
        close = self._mock_close()

        result =\
            exercize.try_execute_transaction_operations([1, 2, 3], 1)

        assert result is True

        start.assert_called_once_with()
        transaction = start.return_value
        execute.assert_has_calls([
            mock.call(transaction, 1),
            mock.call(transaction, 2),
            mock.call(transaction, 3)])
        close.assert_called_once_with(transaction)

    def test_try_transaction_3_times(self):
        start = self._mock_start()
        execute = self._mock_execute()
        close = self._mock_close()

        result =\
            exercize.try_execute_transaction_operations([1, 2, 3], 3)

        assert result is True

        start.assert_called_once_with()
        transaction = start.return_value
        execute.assert_has_calls([
            mock.call(transaction, 1),
            mock.call(transaction, 2),
            mock.call(transaction, 3)])
        close.assert_called_once_with(transaction)

    def test_try_transaction_failing_3_times(self):
        start = self._mock_start(side_effect=iter(['a', 'b', 'c']))
        execute = self._mock_execute(side_effect=RuntimeError)
        close = self._mock_close()

        result =\
            exercize.try_execute_transaction_operations([1, 2, 3], 3)

        assert result is False

        start.assert_has_calls([mock.call()] * 3)
        execute.assert_has_calls([mock.call('a', 1)])
        close.assert_has_calls(
            [mock.call('a'), mock.call('b'), mock.call('c')])

    def test_try_transaction_failing_once(self):
        start = self._mock_start(side_effect=iter(['a', 'b', 'c']))
        execute = self._mock_execute(
            side_effect=iter([RuntimeError, None, None, None]))
        close = self._mock_close()

        result =\
            exercize.try_execute_transaction_operations([1, 2, 3], 3)

        assert result is True

        start.assert_has_calls([mock.call()] * 2)
        execute.assert_has_calls(
            [mock.call('a', 1),
             mock.call('b', 1),
             mock.call('b', 2),
             mock.call('b', 3)])
        close.assert_has_calls([mock.call('a'), mock.call('b')])

    def test_try_transaction_with_other_failure(self):
        start = self._mock_start()
        execute = self._mock_execute(side_effect=SystemExit)
        close = self._mock_close()

        with self.assertRaises(SystemExit):
            exercize.try_execute_transaction_operations([1, 2, 3], 1)

        start.assert_called_once_with()
        transaction = start.return_value
        execute.assert_called_once_with(transaction, 1)
        close.assert_called_once_with(transaction)

    def _mock_start(self, **argkw):
        return self._mock_function(exercize, 'start_transaction', **argkw)

    def _mock_execute(self, **argkw):
        return self._mock_function(
            exercize, 'execute_transaction_operation', **argkw)

    def _mock_close(self):
        return self._mock_function(
            exercize, 'close_transaction')

    def _mock_function(self, obj, name, *args, **kwargs):
        context = mock.patch.object(obj, name, *args, **kwargs)
        result = context.start()
        self.addCleanup(context.stop)
        return result
