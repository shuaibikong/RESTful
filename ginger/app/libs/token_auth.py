from collections import namedtuple

from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,BadSignature,SignatureExpired
from flask import current_app, g, request

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()
User = namedtuple('User',['uid','ac_type','scope'])

@auth.verify_password
def verify_password(token,password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        #类似request g变量的user属性来保存user_info
        g.user = user_info
    return True

def verify_auth_token(token):#解密token
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token) #解密token 如果报错则说明不合法
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    #request 获取要访问的视图函数
    allow = is_in_scope(scope, request.endpoint)#权限验证
    if not allow:
        raise Forbidden()
    return User(uid,ac_type, scope)