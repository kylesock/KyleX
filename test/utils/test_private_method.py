from test.utils.test_suite import KyleXTestSuite
from base.utils import private_method
from base.exchange import Exchange
from base.errors import PermissionDeniedException

import os
import unittest


class TestPrivateMethod(KyleXTestSuite):
    """
    Provides Unit Tests for the private_method decorator
    """

    os.environ['TESTING'] = 'YES'

    def test_valid_admin_private_access(self) -> None:
        """
        Tests VALID private for correct ADMIN user_id and password
        """
        print('')
        print('******test_valid_admin_private_access******')

        @private_method
        def decorated():
            return None

        test_valid_admin_info = Exchange(3, 'test_pwd')
        result = decorated(test_valid_admin_info)
        expected_result = None

        print('\n@private_method\ndecorated(test_valid_admin_info)\n')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertEqual(result, expected_result)

    def test_valid_private_access(self) -> None:
        """
        Tests VALID private for correct USER user_id and password
        """
        print('')
        print('******test_valid_private_access******')

        @private_method
        def decorated():
            return None

        test_valid_private_info = Exchange(2, 'test_pwd')
        result = decorated(test_valid_private_info)
        expected_result = None

        print('\n@private_method\ndecorated(test_valid_private_info)\n')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertEqual(result, expected_result)

    def test_invalid_deactivated_private_access(self) -> None:
        """
        Tests INVALID private for correct DEACTIVATED user_id + password
        """
        print('')
        print('******test_invalid_deactivated_private_access******')

        @private_method
        def decorated():
            return None

        test_deactivated_user_info = Exchange(4, 'test_pwd')

        print('\n@private_method\ndecorated(test_deactivated_user_info)\n')
        print('Expected Output: PermissionDeniedException')
        self.assertRaises(PermissionDeniedException, decorated, test_deactivated_user_info)

    def test_invalid_logged_out_private_access(self) -> None:
        """
        Tests INVALID admin for not logged in user
        """
        print('')
        print('******test_invalid_logged_out_private_access******')

        @private_method
        def decorated():
            return None

        test_invalid_user_info = Exchange()

        print('\n@private_method\ndecorated(test_invalid_user_info)\n')
        print('Expected Output: PermissionDeniedException')
        self.assertRaises(PermissionDeniedException, decorated, test_invalid_user_info)


if __name__ == '__main__':
    unittest.main()
