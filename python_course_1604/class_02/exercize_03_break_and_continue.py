'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

import sys

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
 
    for command in commands:
        # HINT: implement skip and quit commands here before other commands

        if command == 'ping':
            print('pong')
        elif command == 'quit':
            break
        elif command == 'skip':
            continue
        else:
            print('error')


def main():
    lis = sys.argv
    lis.pop(0)
    execute_commands(lis)


if __name__ == "__main__":
    main()
