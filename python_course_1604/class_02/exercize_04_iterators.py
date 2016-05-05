'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Please modify below function to make it behaving as speicified in the
# function documentation.


def execute_commands(commands):
    """ Executes given commands.

    If 'ping' command is given then it prints 'pong'
    In all other it prints 'error'

    The function exits when given sequence of commands terminates.

    Please use break to complete this exercise
    """

    iterator = iter(commands)

    while True:
        # HINT: implement iteration here
        command = next(iterator)

        if command == 'ping':
            print('pong')
        else:
            print('error')
