from rest_framework.exceptions import APIException


class AccountRepeat(APIException):
    status_code = 200
    default_detail = {
        'status': '0001',
        'message': 'Account Name Repeat'
    }
    default_code = None


class ValidateFail(APIException):
    status_code = 200
    default_detail = {
        'status': '0002',
        'message': 'Field Error'
    }
    default_code = None


class Common(APIException):
    pass
