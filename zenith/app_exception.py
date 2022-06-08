from rest_framework.exceptions import APIException

class AppException(APIException):
    result = 'FAIL'
    status_code = 503
    message_code = 'service_unavailable'
    message = 'Service temporarily unavailable, try agin later.'

    def __init__(self, status_code, message_code, message):
        super().__init__(message)
        self.status_code = status_code
        self.message_code = message_code if message_code else self.message_code
        self.message = message if message else self.message
