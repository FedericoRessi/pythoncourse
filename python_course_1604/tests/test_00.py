'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

import sys
import unittest


class TestSetup(unittest.TestCase):

    def test_python_version(self):
        version = sys.version.split()[0].rsplit('.', 1)[0]
        assert version in ['2.7', '3.4']

    def test_python_interpreter_version(self):
        from sh import python  # noqa
        version = str(python('-c', 'import sys; print(sys.version)'))
        assert sys.version == version.rsplit('\n', 1)[0]
