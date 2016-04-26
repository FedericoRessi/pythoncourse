'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Please modify below function to implement quit and skip command to behava as
# speicified in the function documentation.


def execute_commands(commands):
    """ Executes given commands.

    This functions iterates given commands until 'quit' command is received.
    If 'skip' command is given then it is going to skip following command.

    If 'ping' command is given then it prints 'pong'
    In all other it prints 'error'

    Please use both continue and break to complete this exercize
    """
    skip_next_command = False
    for command in commands:
        # HINT: implement skip and quit commands here before other commands

        if skip_next_command:
            skip_next_command = False
            continue
        elif command == 'ping':
            print('pong')
        elif command == 'skip':
            skip_next_command = True
        elif command == 'quit':
            break
        else:
            print('error')
