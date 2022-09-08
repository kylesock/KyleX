from base.utils import load_table
from base.utils import unload_table
from test.test_suite import KyleXTestSuite
from test.test_suite import TEST_USER_TABLE_COPY_FILE_PATH

import unittest


class TestUnloadTable(KyleXTestSuite):
    """
    Unit Tests for the unload_table method
    """

    def test_unload_data_columns(self) -> None:
        """
        Tests that unloading maintains the same format
        """
        print('')
        print('******test_unload_data_columns******')

        unload_table(df=self.test_user_table, path=TEST_USER_TABLE_COPY_FILE_PATH)

        result = load_table(TEST_USER_TABLE_COPY_FILE_PATH)
        expected_result = self.test_user_table
        print(f'unload_data({TEST_USER_TABLE_COPY_FILE_PATH})')
        print(f'resulting table: \n{result}')
        print(f'\nexpected table: \n{expected_result}')
        self.assert_(all(result == expected_result))


if __name__ == '__main__':
    unittest.main()
