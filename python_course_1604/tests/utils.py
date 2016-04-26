'''
Created on 7 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

import unittest
import subprocess


def dont_skip(obj):
    return obj


def skip_if_exercize_not_started(exercize):
    path = exercize.__file__
    if not path.endswith('.py'):
        path = path[:-1]
        assert path.endswith('.py')

    diff = subprocess.check_output(
        ["git", '--no-pager', 'diff', 'master', '--', path])

    if not diff:
        return unittest.skip('Exercize not started: ' + exercize.__file__)

    return dont_skip
