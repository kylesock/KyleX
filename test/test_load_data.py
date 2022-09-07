from base.utils import load_table
from base.utils import unload_table


import unittest

# user table file path - csv
TEST_USER_TABLE_FILE_PATH = '../data/test_user_table.csv'


class TestLoadData(unittest.TestCase):

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

    def __init__(self):
        self.user_table = load_table(path=TEST_USER_TABLE_FILE_PATH)

    def test_load_data_columns(self) -> None:
        """
        Tests the correct columns are present when load_data called
        """
        print('')
        print('******test_load_data_columns******')

        result = list(self.user_table.columns)
        expected_result = ['user_id', 'username', 'password', 'user_type']
        print(f'load_data({TEST_USER_TABLE_FILE_PATH})')
        print(f'resulting headers: {result}')
        print(f'expected headers: {expected_result}')
        self.assertEqual(result, expected_result)

    def test_load_data_not_empty(self) -> None:
        """
        Tests the data is not empty, and in the correct format for processing
        """
        print('')
        print('******test_load_data_not_empty******')

        result = list(self.user_table.loc[2])
        expected_result = ['test_user', 'test_pwd', 'user']
        print(f'load_data({TEST_USER_TABLE_FILE_PATH})')
        print(f'response: {result}')
        print(f'expected response: {expected_result}')
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
