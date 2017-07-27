import os
import sys
import pytest
from kool.db.flat_file import FlatFile

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


class TestFlatFile(object):

	def test_get_permissions(self):
		file = FlatFile()
		filename = '{}/fixtures/users.csv'.format(TEST_DIR)
		result = file.get_permissions(filename)		
		assert isinstance(result, tuple), 'Should return a tuple'