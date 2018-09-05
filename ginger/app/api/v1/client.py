from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError,Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm,UserEmailForm

api = Redprint('client')

@api.route('/register',methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    #验证不通过会抛出异常 不会执行下面代码
    promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email
        }
    promise[form.type.data]()
    return Success() #return一个错误 flask还是会读取get_body和get_headers



def __register_user_by_email():
    form = UserEmailForm().validate_for_api() #可以看出基类的好处
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
