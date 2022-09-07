import unittest
from base.utils import load_table
from base.utils import unload_table

TEST_USER_TABLE_FILE_PATH = '../data/test_user_table.csv'


class KyleXTestSuite(unittest.TestCase):

    test_user_table = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_user_table = load_table(path=TEST_USER_TABLE_FILE_PATH)
        print('')
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        unload_table(df=cls.test_user_table, path=TEST_USER_TABLE_FILE_PATH)
        print('')
        print('tearDownClass')
