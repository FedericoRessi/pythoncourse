'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
@modified by: Gustav Stedje <gustav.stedje@intel.com>
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

    GSt: Could not figure out how this was supposed to work until I looked
         at the test function and realised you were feeding an array of
         commands.
    """
    loopskip = False
    for command in commands:
        # HINT: implement skip and quit commands here before other commands
        if loopskip:
            loopskip = False
            continue
        if command == 'quit':
            break
        elif command == 'skip':
            loopskip = True
            continue
        elif command == 'ping':
            print('pong')
        else:
            print('error')
