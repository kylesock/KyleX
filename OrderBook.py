import pandas as pd
from typing import Optional, Union
import functools


class PermissionDeniedException(Exception):
    # class for rejecting requests to restricted methods without sufficient credentials
    def __init__(self,
                 endpoint: str,
                 user_type: str,
                 permission_required: str) -> None:

        self.endpoint = endpoint
        self.user_type = user_type
        self.permission_required = permission_required

    def __repr__(self) -> str:
        return f"endpoint: {self.endpoint} requires {self.permission_required} permissions, {self.user_type} given."\
               f"Please Login accordingly."

    def __str__(self) -> str:
        return self.__repr__()


def validate_credentials(user_id: int, password: str) -> bool:
    if user_id not in user_db.index:
        return False
    else:
        user_profile = user_db.loc[user_id]
        if (password != user_profile.password) or (user_profile.user_type == 'deactivated'):
            return False

        return True


class Exchange:

    def __init__(self, user_id: Optional[int], password: Optional[str]) -> None:

        self.endpoints: str = 'public'
        self.user_id: Optional[int] = user_id
        self.password: Optional[str] = password
        self.login_status: int = 0 # 0 for not logged in, 1 for logged in

        if self.user_id is not None and self.password is not None:
            valid_login = validate_credentials(self.user_id, self.password)
            if valid_login:
                self.login_status = 1
                if user_db.loc[self.user_id].user_type == 'admin':
                    self.endpoints = 'admin'
                else:
                    self.endpoints = 'private'
                print(f'Welcome {user_db.loc[self.user_id].username}.')
            else:
                print('Invalid username password combination.')

    def user_login(self, user_id: int, password: str) -> str:
        """
        Function to login user, subject to existing in the database and input validation
        :param user_id: Unique User ID to login
        :param password: Password corresponding to the User ID input
        :return: Message of success / fail of login
        """

        if self.login_status == 1:
            return 'Already logged in.'

        valid_login = validate_credentials(user_id, password)
        if valid_login:
            self.login_status = 1
            self.user_id = user_id
            self.password = password

            if user_db.loc[self.user_id].user_type == 'admin':
                self.endpoints = 'admin'
            else:
                self.endpoints = 'private'

            return f'Welcome {user_db.loc[self.user_id].username}.'

        return 'Invalid username password combination.'

    def user_logout(self) -> str:
        """
        Function to logout a user from the session
        :return: Logout message
        """
        if self.login_status == 0:
            return 'Already logged out.'

        self.login_status = 0
        self.user_id = None
        self.password = None
        self.endpoints = 'public'
        return 'Successfully Logged Out.'

    def private_method(self, func):
        """
        Decorator for private methods to block public viewers utilising
        :param func: endpoint being requested by the user
        :return: PermissionDeniedException if not sufficient conditions, else the endpoint is reached as intended
        """
        @functools.wraps(func)
        def wrapper_private_method(*args, **kwargs):
            if self.endpoints in ['private', 'admin']:
                func(*args, **kwargs)
            else:
                raise PermissionDeniedException(endpoint=func.__name__,
                                                user_type=self.endpoints,
                                                permission_required='private')

        return wrapper_private_method

    def admin_method(self, func):
        """
        Decorator for admin methods to block public or privae viewers utilising
        :param func: endpoint being requested by the user
        :return: PermissionDeniedException if not sufficient conditions, else the endpoint is reached as intended
        """
        @functools.wraps(func)
        def wrapper_admin_method(*args, **kwargs):
            if self.endpoints == 'admin':
                func(*args, **kwargs)
            else:
                raise PermissionDeniedException(endpoint=func.__name__,
                                                user_type=self.endpoints,
                                                permission_required='admin')

        return wrapper_admin_method

    @admin_method
    def add_user(self,
                 username: str,
                 password: str,
                 user_type: str = 'user') -> str:
        """
        Method to add a user to the database: Must be an admin to access this endpoint
        :param username: users unique username
        :param password: users password for login
        :param user_type: user type: user or admin
        :return: message on completion / failure of task
        """

        if username in user_db.username:
            return 'username taken, please try another one'

        user_id = max(user_db.index) + 1
        user_db.at[user_id] = [username, password, user_type]
        return f'User {username}(type {user_type}) successfully created.'

    @admin_method
    def delete_user(self,
                    user_id: int,
                    password: str) -> str:
        """
        Remove a User based on their unique ID: Must be an admin and have correct password
        in case of a fat finger error.
        :param user_id: unique user identifier to remove from the database
        :param password: user's password to prevent fat finger deletion from
        :return:
        """

        if user_id not in user_db.index:
            return 'No user id found in database.'

        user_profile = user_db.loc[user_id]

        if password != user_profile.password:
            return 'Incorrect password for this user.'

        user_profile.user_type = 'deactivated'






class Order:
    def __init__(self, user_id: int,
                 instrument_id: int,
                 side: int,
                 ord_type: int,
                 quantity: float,
                 price: float) -> None:
        """

        :param user_id: The Unique User ID
        :param instrument_id: The Unique Instrument ID
        :param side: Side of the Trade. 1 -> BUY, 2 -> SELL
        :param ord_type: Order Type. 1 -> Market Order. 2 -> Limit Order (3, 4 for Stop Market, Stop Limit in future)
        :param quantity: Quantity of the asset being ordered
        :param price: Price of the asset being ordered, ignored if ord_type == 1
        """

        self.user_id = user_id
        self.instrument_id = instrument_id
        self.side = side
        self.ord_type = ord_type
        self.quantity = quantity
        self.price = price

    def __repr__(self) -> str:
        return str(self.__dict__)

    def __str__(self) -> str:
        return self.__repr__()


class MarketOrder(Order):
    def __init__(self, user_id: int,
                 instrument_id: int,
                 side: int,
                 quantity: float,
                 price: float) -> None:
        super(MarketOrder, self).__init__(user_id=user_id,
                                          instrument_id=instrument_id,
                                          side=side,
                                          ord_type=1,
                                          quantity=quantity,
                                          price=price)

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()


class LimitOrder(Order):
    def __init__(self, user_id: int,
                 instrument_id: int,
                 side: int,
                 quantity: float,
                 price: float) -> None:
        super(LimitOrder, self).__init__(user_id=user_id,
                                         instrument_id=instrument_id,
                                         side=side,
                                         ord_type=2,
                                         quantity=quantity,
                                         price=price)

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()


if __name__ == '__main__':

    # Initialise Databases
    user_db = pd.read_csv('user_db.csv', index_col=0)

    # Create new user

    # test_order = Order(2088, 52, 1, 1, 1.0, 20812.12)
    # print(test_order)
    # test_market_order = MarketOrder(2088, 53, 2, 1.25, 53.12)
    # print(test_market_order)
    # test_limit_order = LimitOrder(2088, 53, 2, 1.25, 53.12)
    # print(test_limit_order)
