from test.utils.test_suite import KyleXTestSuite
from base.utils import admin_method
from base.exchange import Exchange
from base.errors import PermissionDeniedException

import unittest


class TestAdminMethod(KyleXTestSuite):
    """
    Provides Unit Tests for the admin_method decorator
    """

    def test_valid_admin_access(self) -> None:
        """
        Tests VALID admin for correct ADMIN user_id and password
        """
        print('')
        print('******test_valid_admin_access******')

        @admin_method
        def decorated():
            return None

        test_valid_user_info = Exchange(3, 'test_pwd')
        result = decorated(test_valid_user_info)
        expected_result = None

        print('\n@admin_method\ndecorated(test_valid_user_info)\n')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertEqual(result, expected_result)

    def test_invalid_user_admin_access(self) -> None:
        """
        Tests INVALID admin for correct USER user_id + password
        """
        print('')
        print('******test_invalid_user_admin_access******')

        @admin_method
        def decorated():
            return None

        test_invalid_user_info = Exchange(2, 'test_pwd')

        print('\n@admin_method\ndecorated(test_invalid_user_info)\n')
        print('Expected Output: PermissionDeniedException')
        self.assertRaises(PermissionDeniedException, decorated, test_invalid_user_info)

    def test_invalid_deactivated_admin_access(self) -> None:
        """
        Tests INVALID admin for correct DEACTIVATED user_id + password
        """
        print('')
        print('******test_invalid_deactivated_admin_access******')

        @admin_method
        def decorated():
            return None

        test_deactivated_user_info = Exchange(4, 'test_pwd')

        print('\n@admin_method\ndecorated(test_deactivated_user_info)\n')
        print('Expected Output: PermissionDeniedException')
        self.assertRaises(PermissionDeniedException, decorated, test_deactivated_user_info)

    def test_invalid_logged_out_admin_access(self) -> None:
        """
        Tests INVALID admin for not logged in user
        """
        print('')
        print('******test_invalid_logged_out_admin_access******')

        @admin_method
        def decorated():
            return None

        test_invalid_user_info = Exchange()

        print('\n@admin_method\ndecorated(test_invalid_user_info)\n')
        print('Expected Output: PermissionDeniedException')
        self.assertRaises(PermissionDeniedException, decorated, test_invalid_user_info)


if __name__ == '__main__':
    unittest.main()
