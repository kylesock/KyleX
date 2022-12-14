from base.utils import load_table
from base.utils import unload_table

import unittest
import os

TEST_USER_TABLE_FILE_PATH = '/Users/kylesock/PycharmProjects/KyleX/data/test_user_table.csv'
TEST_USER_TABLE_COPY_FILE_PATH = '/Users/kylesock/PycharmProjects/KyleX/data/test_user_table_copy.csv'


class KyleXTestSuite(unittest.TestCase):
    """
    Base Test Suite for the Application
    """

    test_user_table = None
    os.environ['TESTING'] = 'NO'

    @classmethod
    def setUpClass(cls) -> None:
        """
        Provides setup to load in user table on instantiation
        """
        cls.test_user_table = load_table(path=TEST_USER_TABLE_FILE_PATH)
        print('')
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Updates user table csv and unloads it from memory
        """
        unload_table(df=cls.test_user_table, path=TEST_USER_TABLE_FILE_PATH)
        print('')
        print('tearDownClass')
