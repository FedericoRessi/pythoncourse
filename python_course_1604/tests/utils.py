'''
Created on 7 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

import unittest


def dont_skip(obj):
    return obj


def skip_if_exercize_not_started(exercize):
    path = exercize.__file__
    if not path.endswith('.py'):
        path = path[:-1]
        assert path.endswith('.py')

    from sh import git

    diff = str(git('--no-pager', 'diff', 'master', '--', path))
    print(diff)
    if diff:
        return unittest.skip('Exercize not started: ' + exercize.__file__)

    return dont_skip
