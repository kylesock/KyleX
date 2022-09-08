from test.utils.test_suite import KyleXTestSuite
from test.utils.test_suite import TEST_USER_TABLE_FILE_PATH
from base.exchange import Exchange

import pandas as pd
import unittest


class TestInit(KyleXTestSuite):

    def test_table_loading(self) -> None:
        """
        Tests user_table loaded when instantiating class
        """
        print('')
        print('******test_table_loading******')

        test_prod_mock_session = Exchange()
        self.assertIsNotNone(test_prod_mock_session.user_table)

    def test_privilege_no_login(self) -> None:
        """
        Tests endpoints access is PUBLIC for non-logged-in user
        """
        print('')
        print('******test_privilege_no_login******')

        test_prod_mock_session = Exchange()
        self.assertEqual(test_prod_mock_session.endpoints, 'public')

    def test_privilege_deactivated(self) -> None:
        """
        Tests endpoints access is PUBLIC for deactivated user
        """
        print('')
        print('******test_privilege_deactivated******')

        test_prod_mock_session = Exchange(4, 'test_pwd')
        self.assertEqual(test_prod_mock_session.endpoints, 'public')

    def test_privilege_user(self) -> None:
        """
        Tests endpoints access is PRIVATE for logged-in user
        """
        print('')
        print('******test_privilege_user******')

        test_prod_mock_session = Exchange(2, 'test_pwd')
        self.assertEqual(test_prod_mock_session.endpoints, 'private')

    def test_privilege_admin(self) -> None:
        """
        Tests endpoints access is ADMIN for logged-in admin
        """
        print('')
        print('******test_privilege_admin******')

        test_prod_mock_session = Exchange(3, 'test_pwd')
        self.assertEqual(test_prod_mock_session.endpoints, 'admin')

    def test_login_status_no_login(self) -> None:
        """
        Tests login_status for non-logged-in user
        """
        print('')
        print('******test_login_status_no_login******')

        test_prod_mock_session = Exchange()
        self.assertEqual(test_prod_mock_session.login_status, 0)

    def test_login_status_invalid_user(self) -> None:
        """
        Tests login_status for invalid user credentials
        """
        print('')
        print('******test_login_status_invalid_user******')

        test_prod_mock_session = Exchange(-1, 'test_pwd')
        self.assertEqual(test_prod_mock_session.login_status, 0)

    def test_login_status_invalid_password(self) -> None:
        """
        Tests login_status for invalid user password combination
        """
        print('')
        print('******test_login_status_invalid_password******')

        test_prod_mock_session = Exchange(2, 'invalid_test_pwd')
        self.assertEqual(test_prod_mock_session.login_status, 0)

    def test_login_status_deactivated_login(self) -> None:
        """
        Tests login_status for invalid user credentials
        """
        print('')
        print('******test_login_status_deactivated_login******')

        test_prod_mock_session = Exchange(4, 'test_pwd')
        self.assertEqual(test_prod_mock_session.login_status, 0)

    def test_login_status_valid_user(self) -> None:
        """
        Tests login_status for non-logged-in user
        """
        print('')
        print('******test_login_status_valid_user******')

        test_prod_mock_session = Exchange(2, 'test_pwd')
        self.assertEqual(test_prod_mock_session.login_status, 1)

    def test_login_status_valid_admin(self) -> None:
        """
        Tests login_status for non-logged-in admin
        """
        print('')
        print('******test_login_status_valid_admin******')

        test_prod_mock_session = Exchange(3, 'test_pwd')
        self.assertEqual(test_prod_mock_session.login_status, 1)


class TestRepr(KyleXTestSuite):

    def test_no_login_repr(self) -> None:
        """
        Tests the __repr__ format for non-logged-in user
        """
        print('')
        print('******test_no_login_repr******')

        test_prod_mock_session = Exchange()
        expected_result = str({'login_status': test_prod_mock_session.login_status, 'user_id': test_prod_mock_session.user_id,
                               'password': test_prod_mock_session.password, 'endpoints': test_prod_mock_session.endpoints})

        self.assertEqual(test_prod_mock_session.__repr__(), expected_result)

    def test_user_login_repr(self) -> None:
        """
        Tests the __repr__ format for logged-in user
        """
        print('')
        print('******test_user_login_repr******')

        test_prod_mock_session = Exchange(2, 'test_pwd')
        expected_result = str(
            {'login_status': test_prod_mock_session.login_status, 'user_id': test_prod_mock_session.user_id,
             'password': test_prod_mock_session.password, 'endpoints': test_prod_mock_session.endpoints})

        self.assertEqual(test_prod_mock_session.__repr__(), expected_result)

    def test_admin_login_repr(self) -> None:
        """
        Tests the __repr__ format for admin
        """
        print('')
        print('******test_admin_login_repr******')

        test_prod_mock_session = Exchange(3, 'test_pwd')
        expected_result = str(
            {'login_status': test_prod_mock_session.login_status, 'user_id': test_prod_mock_session.user_id,
             'password': test_prod_mock_session.password, 'endpoints': test_prod_mock_session.endpoints})

        self.assertEqual(test_prod_mock_session.__repr__(), expected_result)

    def test_deactivated_login_repr(self) -> None:
        """
        Tests the __repr__ format for deactivated user
        """
        print('')
        print('******test_deactivated_login_repr******')

        test_prod_mock_session = Exchange(4, 'test_pwd')
        expected_result = str(
            {'login_status': test_prod_mock_session.login_status, 'user_id': test_prod_mock_session.user_id,
             'password': test_prod_mock_session.password, 'endpoints': test_prod_mock_session.endpoints})

        self.assertEqual(test_prod_mock_session.__repr__(), expected_result)


class TestStr(KyleXTestSuite):

    def test_no_login_str(self) -> None:
        """
        Tests the __str__ format for non-logged-in user
        """
        print('')
        print('******test_no_login_str******')

        test_prod_mock_session = Exchange()
        expected_result = str(
            {'login_status': test_prod_mock_session.login_status, 'user_id': test_prod_mock_session.user_id,
             'password': test_prod_mock_session.password, 'endpoints': test_prod_mock_session.endpoints})

        self.assertEqual(test_prod_mock_session.__str__(), expected_result)

    def test_user_login_str(self) -> None:
        """
        Tests the __str__ format for logged-in user
        """
        print('')
        print('******test_user_login_str******')

        test_prod_mock_session = Exchange(2, 'test_pwd')
        expected_result = str(
            {'login_status': test_prod_mock_session.login_status, 'user_id': test_prod_mock_session.user_id,
             'password': test_prod_mock_session.password, 'endpoints': test_prod_mock_session.endpoints})

        self.assertEqual(test_prod_mock_session.__str__(), expected_result)

    def test_admin_login_str(self) -> None:
        """
        Tests the __str__ format for admin
        """
        print('')
        print('******test_admin_login_str******')

        test_prod_mock_session = Exchange(3, 'test_pwd')
        expected_result = str(
            {'login_status': test_prod_mock_session.login_status, 'user_id': test_prod_mock_session.user_id,
             'password': test_prod_mock_session.password, 'endpoints': test_prod_mock_session.endpoints})

        self.assertEqual(test_prod_mock_session.__str__(), expected_result)

    def test_deactivated_login_str(self) -> None:
        """
        Tests the __str__ format for deactivated user
        """
        print('')
        print('******test_deactivated_login_str******')

        test_prod_mock_session = Exchange(4, 'test_pwd')
        expected_result = str(
            {'login_status': test_prod_mock_session.login_status, 'user_id': test_prod_mock_session.user_id,
             'password': test_prod_mock_session.password, 'endpoints': test_prod_mock_session.endpoints})

        self.assertEqual(test_prod_mock_session.__str__(), expected_result)


class TestUserLogin(KyleXTestSuite):

    def test_invalid_user_user_login(self) -> None:
        """
        Tests invalid user_id attempt to log in
        """
        print('')
        print('******test_invalid_user_user_login******')

        test_prod_mock_session = Exchange()
        result = test_prod_mock_session.user_login(-1, 'test_pwd')
        expected_result = 'Invalid username password combination.'
        self.assertEqual(result, expected_result)
        self.assertIsNone(test_prod_mock_session.user_id)
        self.assertIsNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 0)
        self.assertEqual(test_prod_mock_session.endpoints, 'public')

    def test_invalid_password_user_login(self) -> None:
        """
        Tests invalid password for a given user
        """
        print('')
        print('******test_invalid_password_user_login******')

        test_prod_mock_session = Exchange()
        result = test_prod_mock_session.user_login(2, 'invalid_test_pwd')
        expected_result = 'Invalid username password combination.'
        self.assertEqual(result, expected_result)
        self.assertIsNone(test_prod_mock_session.user_id)
        self.assertIsNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 0)
        self.assertEqual(test_prod_mock_session.endpoints, 'public')

    def test_already_logged_in_user_login(self) -> None:
        """
        Tests response to log in request when already logged-in
        """
        print('')
        print('******test_already_logged_in_user_login******')

        test_prod_mock_session = Exchange(2, 'test_pwd')
        result = test_prod_mock_session.user_login(2, 'test_pwd')
        expected_result = 'Already logged in.'
        self.assertEqual(result, expected_result)
        self.assertIsNotNone(test_prod_mock_session.user_id)
        self.assertIsNotNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 1)
        self.assertEqual(test_prod_mock_session.endpoints, 'private')

    def test_deactivated_account_user_login(self) -> None:
        """
        Tests response when an INVALID log-in attempt from DEACTIVATED user
        """
        print('')
        print('******test_deactivated_account_user_login******')

        test_prod_mock_session = Exchange()
        result = test_prod_mock_session.user_login(4, 'test_pwd')
        expected_result = 'Invalid username password combination.'
        self.assertEqual(result, expected_result)
        self.assertIsNone(test_prod_mock_session.user_id)
        self.assertIsNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 0)
        self.assertEqual(test_prod_mock_session.endpoints, 'public')

    def test_valid_user_user_login(self) -> None:
        """
        Tests response when a VALID log-in attempt from USER
        """
        print('')
        print('******test_valid_user_user_login******')

        test_prod_mock_session = Exchange()
        result = test_prod_mock_session.user_login(2, 'test_pwd')
        expected_result = f'Welcome {test_prod_mock_session.user_table.loc[test_prod_mock_session.user_id].username}.'
        self.assertEqual(result, expected_result)
        self.assertIsNotNone(test_prod_mock_session.user_id)
        self.assertIsNotNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 1)
        self.assertEqual(test_prod_mock_session.endpoints, 'private')

    def test_valid_admin_user_login(self) -> None:
        """
        Tests response when a VALID log-in attempt from ADMIN
        """
        print('')
        print('******test_valid_admin_user_login******')

        test_prod_mock_session = Exchange()
        result = test_prod_mock_session.user_login(3, 'test_pwd')
        expected_result = f'Welcome {test_prod_mock_session.user_table.loc[test_prod_mock_session.user_id].username}.'
        self.assertEqual(result, expected_result)
        self.assertIsNotNone(test_prod_mock_session.user_id)
        self.assertIsNotNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 1)
        self.assertEqual(test_prod_mock_session.endpoints, 'admin')


class TestUserLogout(KyleXTestSuite):

    def test_already_logged_out_user_logout(self) -> None:
        """
        Tests response to log out request when already logged-out
        """
        print('')
        print('******test_already_logged_out_user_logout******')

        test_prod_mock_session = Exchange()
        result = test_prod_mock_session.user_logout()
        expected_result = 'Already logged out.'
        self.assertEqual(result, expected_result)
        self.assertIsNone(test_prod_mock_session.user_id)
        self.assertIsNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 0)
        self.assertEqual(test_prod_mock_session.endpoints, 'public')

    def test_user_user_logout(self) -> None:
        """
        Tests response for logged-in user logout
        """
        print('')
        print('******test_user_user_logout******')

        test_prod_mock_session = Exchange(2, 'test_pwd')
        result = test_prod_mock_session.user_logout()
        expected_result = 'Successfully Logged Out.'
        self.assertEqual(result, expected_result)
        self.assertIsNone(test_prod_mock_session.user_id)
        self.assertIsNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 0)
        self.assertEqual(test_prod_mock_session.endpoints, 'public')

    def test_admin_user_logout(self) -> None:
        """
        Tests response for logged-in admin logout
        """
        print('')
        print('******test_admin_user_logout******')

        test_prod_mock_session = Exchange(3, 'test_pwd')
        result = test_prod_mock_session.user_logout()
        expected_result = 'Successfully Logged Out.'
        self.assertEqual(result, expected_result)
        self.assertIsNone(test_prod_mock_session.user_id)
        self.assertIsNone(test_prod_mock_session.password)
        self.assertEqual(test_prod_mock_session.login_status, 0)
        self.assertEqual(test_prod_mock_session.endpoints, 'public')


class TestAddUser(KyleXTestSuite):

    def test_user_taken_add_user(self) -> None:
        """
        Tests response to add_user when username already exists
        """
        print('')
        print('******test_user_taken_add_user******')

        test_prod_mock_session = Exchange(3, 'test_pwd')
        initial_table = test_prod_mock_session.user_table.copy()

        result = test_prod_mock_session.add_user(
                                                 username='test_user',
                                                 password='new_test_pwd',
                                                 user_type='admin')
        expected_result = 'Username taken, please try another one.'

        self.assertEqual(result, expected_result)
        self.assertTrue(initial_table.equals(test_prod_mock_session.user_table))

    def test_new_user_add_user(self) -> None:
        """
        Tests expected response to add_user for USER account
        """
        print('')
        print('******test_new_user_add_user******')

        test_prod_mock_session = Exchange(3, 'test_pwd')
        initial_table = test_prod_mock_session.user_table.copy()
        new_user_details = ['new_test_user', 'new_test_pwd', 'user']

        result = test_prod_mock_session.add_user(username=new_user_details[0],
                                                 password=new_user_details[1],
                                                 user_type=new_user_details[2])
        expected_result = f'User {new_user_details[0]}(type {new_user_details[2]}) successfully created.'

        self.assertEqual(result, expected_result)
        self.assertTrue(initial_table.equals(test_prod_mock_session.user_table.iloc[:-1]))
        test_prod_mock_session.user_table = initial_table.copy()

    def test_new_admin_add_user(self) -> None:
        """
        Tests expected response to add_user for ADMIN account
        """
        print('')
        print('******test_new_admin_add_user******')

        test_prod_mock_session = Exchange(3, 'test_pwd')
        initial_table = test_prod_mock_session.user_table.copy()
        new_admin_details = ['new_test_user', 'new_test_pwd', 'admin']

        result = test_prod_mock_session.add_user(username=new_admin_details[0],
                                                 password=new_admin_details[1],
                                                 user_type=new_admin_details[2])
        expected_result = f'User {new_admin_details[0]}(type {new_admin_details[2]}) successfully created.'

        self.assertEqual(result, expected_result)
        self.assertTrue(initial_table.equals(test_prod_mock_session.user_table.iloc[:-1]))
        test_prod_mock_session.user_table = initial_table.copy()


if __name__ == '__main__':
    unittest.main()
