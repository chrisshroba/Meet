__author__ = 'chrisshroba'


class LoginException(Exception):
    type = None
    message = None
    data = None

    error_obj = {
        "status": "error",
        "data": {
            "type": type or "login",
            "message": message or "No additional information available",
            "data": data or {}
        }
    }

    def __init__(self, type=None, message=None, data = None):
        self.type = type
        self.message = message
        self.data = data

    USERNAME_NOT_FOUND = 1
    INCORRECT_PASSWORD = 2