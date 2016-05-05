'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Please modify below function to make it behaving as speicified in the
# function documentation.


def execute_commands(commands):
    """ Executes given commands.

    This functions iterates given commands until 'quit' command is received.

    If 'skip' command is given then it is going to skip following command.

    If 'ping' command is given then it prints 'pong'

    In all other cases it prints 'error'

    Please use both continue and break to complete this exercise
    """

    for command in commands:
        # HINT: threat skip and quit commands here

        if command == 'ping':
            print('pong')
        else:
            print('error')
