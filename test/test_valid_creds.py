from base.utils import validate_credentials
from test.test_suite import KyleXTestSuite

import unittest


class TestValidCreds(KyleXTestSuite):

    def test_valid_creds_valid_user(self) -> None:
        """
        Tests A TRUE flag given when VALID user inputs username & password
        """
        print('')
        print('******test_valid_creds_valid_user******')

        test_user_id, test_password = 2, 'test_pwd'
        result = validate_credentials(table=self.test_user_table,
                                      user_id=test_user_id, password=test_password)
        expected_result = True
        print(f'validate_credentials(self.test_user_table,{test_user_id}, {test_password})')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertTrue(result)

    def test_valid_creds_deactivated_user(self) -> None:
        """
        Tests a FALSE flag given DEACTIVATED user inputs VALID username & password
        """
        print('')
        print('******test_valid_creds_deactivated_user******')

        test_user_id, test_password = 4, 'test_pwd'
        result = validate_credentials(table=self.test_user_table,
                                      user_id=test_user_id, password=test_password)
        expected_result = False
        print(f'validate_credentials(self.test_user_table,{test_user_id}, {test_password})')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertFalse(result)

    def test_valid_creds_invalid_user(self) -> None:
        """
        Tests a FALSE flag given when INVALID user id
        """
        print('')
        print('******test_valid_creds_invalid_user******')

        test_user_id, test_password = -1, 'test_pwd'
        result = validate_credentials(table=self.test_user_table,
                                      user_id=test_user_id, password=test_password)
        expected_result = False
        print(f'validate_credentials(self.test_user_table,{test_user_id}, {test_password})')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertFalse(result)

    def test_valid_creds_invalid_pwd(self) -> None:
        """
        Tests a FALSE flag given when VALID user but INVALID password
        """
        print('')
        print('******test_valid_creds_invalid_pwd******')

        test_user_id, test_password = 2, 'invalid_test_pwd'
        result = validate_credentials(table=self.test_user_table,
                                      user_id=test_user_id, password=test_password)
        expected_result = False
        print(f'validate_credentials(self.test_user_table,{test_user_id}, {test_password})')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertFalse(result)

    def test_valid_creds_both_empty(self) -> None:
        """
        Tests that a False flag given when empty credentials passed
        """
        print('')
        print('******test_valid_creds_both_empty******')

        test_user_id, test_password = 0, ''
        result = validate_credentials(table=self.test_user_table,
                                      user_id=test_user_id, password=test_password)
        expected_result = False
        print(f'validate_credentials(self.test_user_table,{test_user_id}, {test_password})')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertFalse(result)

    def test_valid_creds_no_password(self) -> None:
        """
        Tests that a False flag is given when no password provided
        """
        print('')
        print('******test_valid_creds_no_password******')

        test_user_id, test_password = 2, ''
        result = validate_credentials(table=self.test_user_table,
                                      user_id=test_user_id, password=test_password)
        expected_result = False
        print(f'validate_credentials(self.test_user_table,{test_user_id}, {test_password})')
        print(f'result: {result}')
        print(f'expected result: {expected_result}')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
