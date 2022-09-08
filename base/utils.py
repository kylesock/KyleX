import pandas as pd
from functools import wraps
from base.errors import PermissionDeniedException
import os

__all__ = [
    'load_table',
    'unload_table',
    'validate_credentials',
    'admin_method',
    'private_method'
]


# load user table from file path
def load_table(path: str) -> pd.DataFrame:
    """
    Loads the User Table for Authorisation to reach private and admin endpoints.
    """
    # open user table csv file
    df = pd.read_csv(path, index_col=0)
    print('Table Loaded.')
    return df


# unload user table to file path
def unload_table(df: pd.DataFrame, path: str) -> None:
    """
    Unloads the User Table Object, saving any changes back to the csv
    """
    df.to_csv(path)
    print('Table Unloaded')


def validate_credentials(table: pd.DataFrame, user_id: int, password: str) -> bool:
    if user_id not in table.index:
        return False
    else:
        user_profile = table.loc[user_id]
        if (password != user_profile.password) or (user_profile.user_type == 'deactivated'):
            return False

        return True


def testing_guard(decorator_func):
    """
    Decorator that only applies another decorator if the TESTING environment
    variable is not set.

    Args:
        decorator_func: The decorator function.

    Returns:
        Function that calls a function after applying the decorator if TESTING
        environment variable is not set and calls the plain function if it is set.
    """

    def replacement(original_func):
        """Function that is called instead of original function."""

        def apply_guard(*args, **kwargs):
            """Decides whether to use decorator on function call."""
            if os.getenv('TESTING') is not None:
                return original_func(*args, **kwargs)
            return decorator_func(original_func)(*args, **kwargs)

        return apply_guard

    return replacement


@testing_guard
def admin_method(func):
    """
    Decorator for admin methods to block public or private viewers utilising
    :param func: endpoint being requested by the user
    :return: PermissionDeniedException if not sufficient conditions, else the endpoint is reached as intended
    """

    @wraps(func)
    def wrapper_admin_method(self, *args, **kwargs):
        if self.endpoints == 'admin':
            func(*args, **kwargs)
        else:
            raise PermissionDeniedException(endpoint=func.__name__,
                                            user_type=self.endpoints,
                                            permission_required='admin')

    return wrapper_admin_method


@testing_guard
def private_method(func):
    """
    Decorator for private methods to block public viewers utilising
    :param func: endpoint being requested by the user
    :return: PermissionDeniedException if not sufficient conditions, else the endpoint is reached as intended
    """

    @wraps(func)
    def wrapper_private_method(self, *args, **kwargs):
        if self.endpoints in ['private', 'admin']:
            func(*args, **kwargs)
        else:
            raise PermissionDeniedException(endpoint=func.__name__,
                                            user_type=self.endpoints,
                                            permission_required='private')

    return wrapper_private_method
