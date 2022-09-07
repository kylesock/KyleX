
class BaseError(Exception):
    pass


class PermissionDeniedException(BaseError):
    # class for rejecting requests to restricted methods without sufficient credentials
    def __init__(self,
                 endpoint: str,
                 user_type: str,
                 permission_required: str) -> None:

        self.endpoint = endpoint
        self.user_type = user_type
        self.permission_required = permission_required

    def __repr__(self) -> str:
        return f"endpoint: {self.endpoint} requires {self.permission_required} permissions, {self.user_type} given." \
               f"Please Login accordingly."

    def __str__(self) -> str:
        return self.__repr__()


__all__ = [
    'BaseError',
    'PermissionDeniedException'
]