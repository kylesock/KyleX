from test.test_suite import KyleXTestSuite
from test.test_suite import TEST_USER_TABLE_FILE_PATH

import unittest


class TestPrivateMethod(KyleXTestSuite):
    """
    Provides Unit Tests for the private_method decorator
    """
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
