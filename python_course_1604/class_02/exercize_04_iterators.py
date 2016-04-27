'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Please modify below function to implement quit and skip command to behava as
# speicified in the function documentation.


def execute_commands(commands):
    """ Executes given commands.

    If 'ping' command is given then it prints 'pong'
    In all other it prints 'error'

    The function exits when given sequence of commands terminates.

    Please use both continue and break to complete this exercize
    """

    iterator = iter(commands)

    skip_flag = False

    while True:
        # HINT: look how next function behave when sequence terminates

        try:
            command = next(iterator)
        except StopIteration:
            break

        if skip_flag:
            skip_flag = False
            continue
        elif command == 'skip':
            skip_flag = True
        elif command == 'ping':
            print('pong')
        else:
            print('error')
