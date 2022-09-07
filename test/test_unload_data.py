from base.utils import load_table
from base.utils import unload_table
from test.test_suite import KyleXTestSuite
from test.test_suite import TEST_USER_TABLE_FILE_PATH

import unittest
import pandas as pd

class TestUnloadData(KyleXTestSuite):

    def test_unload_data_columns(self) -> None:
        """
        Tests that unloading maintains the same format
        """
        print('')
        print('******test_unload_data_columns******')

        compare_file_path = TEST_USER_TABLE_FILE_PATH[:-4] + '_copy.csv'
        unload_table(df=self.test_user_table, path=compare_file_path)

        result = load_table(compare_file_path)
        expected_result = self.test_user_table
        print(f'unload_data({compare_file_path})')
        print(f'resulting table: \n{result}')
        print(f'\nexpected table: \n{expected_result}')
        self.assert_(all(result == expected_result))


if __name__ == '__main__':
    unittest.main()
