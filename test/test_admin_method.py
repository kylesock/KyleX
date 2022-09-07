from test.test_suite import KyleXTestSuite
from base.utils import admin_method
from base.exchange import Exchange

import unittest


class TestAdminMethod(KyleXTestSuite):
    """
    Provides Unit Tests for the admin_method decorator
    """

    def test_valid_admin_access(self):
        @admin_method
        def to_be_decorated(user_id: int, password: str):
            user_profile = self.test_user_table.loc[user_id]
            assert user_profile.user_type == 'admin'
            assert user_profile.password == password

        session = Exchange(3, 'test_pwd')
        to_be_decorated(session)


if __name__ == '__main__':
    unittest.main()
