'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

import random


def start_transaction():
    """ Starts a new transaction returning transaction number
    """

    return random.randint(1, 1000)


def execute_transaction_operation(transaction_number, operation):
    """ It tryes to do some operation

    Parameters:
        - transaction_number: number returned by start_transaction
        - operation: something to do in the transaction

    It raises:
        - RuntimeError: in case of operation error
    """


def close_transaction(transaction_number):
    """ Closes a transaction

    Parameters:
        - transaction_number: number returned by start_transaction
    """


# Please modify below function to make it behaving as speicified in the
# function documentation.

def try_execute_transaction_operations(operations, max_attempts):
    """
    Try executing given transaction operations

    It creates a new tranzaction and try executing all given operations
    When an operation fails it closes the transaction and retry again up to
    max_attempts times.

    TODO: Please FIX following bug:

    It has been discovered that transaction are not properly closed when
    an unspecified exception other than RuntimeError
    (like for example SystemExit) is raised during transaction operation
    execution. In such case transaction has to be cloesed but without capuring
    any undefined exception. Hint: use finally statement.
    """

    # Tries max_attempts times
    for _ in range(max_attempts):
        transaction = start_transaction()
        try:
            # try executing all transaction operations
            for operation in operations:
                execute_transaction_operation(transaction, operation)

        except RuntimeError:
            # failed operation
            continue # retry!

        else:
            return True  # transaction has been completed with success

        finally:
            # finally close the transaction
            close_transaction(transaction)

    # Failed to complet transaction after max_attempts
    return False
