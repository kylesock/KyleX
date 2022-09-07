from test.test_suite import KyleXTestSuite
from test.test_suite import TEST_USER_TABLE_FILE_PATH

import unittest


class TestLoadData(KyleXTestSuite):

    def test_load_data_columns(self) -> None:
        """
        Tests the correct columns are present when load_data called
        """
        print('')
        print('******test_load_data_columns******')

        result = list(self.test_user_table.columns)
        expected_result = ['username', 'password', 'user_type']
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

        result = list(self.test_user_table.loc[2])
        expected_result = ['test_user', 'test_pwd', 'user']
        print(f'load_data({TEST_USER_TABLE_FILE_PATH})')
        print(f'response: {result}')
        print(f'expected response: {expected_result}')
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
