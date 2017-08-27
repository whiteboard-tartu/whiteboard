# import os
# import sys
# import pytest
# from kool.db.flat_file import FlatFile
# from kool.core.exceptions import UserNotFound

# TEST_DIR = os.path.dirname(os.path.abspath(__file__))


# class TestFlatFile(object):

# 	@classmethod
# 	def setup_class(cls):
# 		cls.file = FlatFile()

# 	def test_get_permissions(self):
# 		filename = '{}/fixtures/users.csv'.format(TEST_DIR)
# 		result = self.file.get_permissions(filename)
# 		assert isinstance(result, tuple), 'Should return a tuple'
# 		assert isinstance(result[0], list), 'First item should be a list'
# 		assert isinstance(result[1], dict), 'Last item should be a dict'

# 	def test_add_user(self):
# 		username = 'johndoe'
# 		realname = 'John Doe'
# 		password = 'test_pwd'
# 		permissions = 'student'
# 		filename = '{}/fixtures/users.csv'.format(TEST_DIR)
# 		self.file.add_user(username, realname, password, 
# 			permissions, filename)
# 		result = self.file.get_permissions(filename)
# 		assert result[1]['johndoe'] == (realname, password, permissions) 

# 	def test_delete_user(self):
# 		username = 'johndoe'
# 		filename = '{}/fixtures/users.csv'.format(TEST_DIR)

# 		self.file.delete_user(username, filename)
		
# 		result = self.file.get_permissions(filename)
# 		expected = {'ao': ('Antony Orenge', 'aopwd', 'teacher \n'), 
# 					'bm': ('Benson Muite', 'bmpwd', 'student\n'), 
# 					'gg': ('Geraldine Granada', 'ggpwd', 'teacher\n')}
# 		assert len(result[1]) == 3
# 		assert result[1] == expected

# 	def test_delete_user_raises_exception(self):
# 		username = 'marydoe'
# 		filename = '{}/fixtures/users.csv'.format(TEST_DIR)

# 		with pytest.raises(UserNotFound):
# 			self.file.delete_user(username, filename)