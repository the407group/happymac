#
# TODO: Fix tests, needs work on Auger's automatic test generator
#
from collections import defaultdict
import log
from mock import patch
import os
import os.path
import preferences
import process
import psutil
from psutil import Popen
import sys
import unittest
import utils
import versions.v00001.process
import versions.v00001.suspender
from versions.v00001.suspender import defaultdict
import versions.v00001.utils
from versions.v00001.utils import OnMainThread


class PreferencesTest(unittest.TestCase):
    def test_get(self):
        self.assertEqual(
            preferences.get(default=None,key='suspend - Electron'),
            None
        )


    @patch.object(os.path, 'expanduser')
    @patch.object(os.path, 'join')
    @patch.object(os.path, 'exists')
    def test_get_preferences_path(self, mock_exists, mock_join, mock_expanduser):
        mock_exists.return_value = True
        mock_join.return_value = '/Users/chris/HappyMacApp/downloads/v00001'
        mock_expanduser.return_value = '/Users/chris'
        self.assertEqual(
            preferences.get_preferences_path(),
            '/Users/chris/HappyMacApp/happymac.prefs'
        )


    @patch.object(log, 'log')
    def test_set(self, mock_log):
        mock_log.return_value = None
        self.assertEqual(
            preferences.set(value=True,key='suspend - qemu-system-i386'),
            None
        )


if __name__ == "__main__":
    unittest.main()
