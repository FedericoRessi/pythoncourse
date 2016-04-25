'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

import subprocess
import sys
import unittest


class TestSetup(unittest.TestCase):

    def test_python_version(self):
        version, _ = sys.version.split()[0].rsplit('.', 1)
        assert version in ['2.7', '3.4']

    def test_python_interpreter_version(self):
        actual_version, _ = subprocess.check_output(
            ['python', '-c', 'import sys; print(sys.version)']
        ).decode('utf8').rsplit('\n', 1)

        assert sys.version == actual_version.strip()
