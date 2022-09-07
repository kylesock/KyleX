import unittest
from base.utils import load_table
from base.utils import unload_table

TEST_USER_TABLE_FILE_PATH = '../data/test_user_table.csv'


class KyleXTestSuite(unittest.TestCase):
    """
    Base Test Suite for the Application
    """

    test_user_table = None

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
