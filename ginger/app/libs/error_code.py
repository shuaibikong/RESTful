from app.libs.error import APIException

class Success(APIException): #利用APIException的处理机制来处理成功的信息 又可以保证前端得到的数据一致
    code = 200
    msg = 'OK'
    error_code = 0

class DeleteSuccess(Success):
    code = 202
    error_code = 1

class ServerError(APIException):
    code = 500
    msg = 'sorry.we made a mistake'
    error_code = 999


class ClientTypeError(APIException): #自定义一个ClientTypeError类抛出自己的异常
    code = 400
    msg = (
        'client is invalid'
    )
    error_code = 1006

class ParameterException(APIException):
    code = 400
    msg = 'invalid paramet'
    error_code = 1000

class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found 0__0...'
    error_code = 1001

class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005

class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'

class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'