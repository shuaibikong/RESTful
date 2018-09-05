from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data =request.get_json(silent=True) #在这里重写父类的初始化方法 实现每次调用form时自动传参
        args = request.args.to_dict()
        super(BaseForm,self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm,self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self #这里返回一个form 可以不用再实例化form而直接执行校验
