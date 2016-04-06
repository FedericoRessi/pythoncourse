'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

import sys
import unittest


class TestSetup(unittest.TestCase):

    def test_python_version(self):
        assert sys.version.split()[0].rsplit('.', 1)[0] in ['2.7', '3.4']
