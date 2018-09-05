from wtforms import StringField,IntegerField,ValidationError
from wtforms.validators import DataRequired, Length, Regexp, Email
from app.validators.base import BaseForm as Form
from app.libs.enums import ClientTypeEnum
from app.models.user import User



class ClientForm(Form): #所有客户端共同的特性都经过ClientForm来处理 ,处理后在每个函数中处理自己的特色功能
    account = StringField(validators=[DataRequired('不允许为空'),Length(5,32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()]) # 用数字代表客户端类型,必须为支持的枚举类型

    def validate_type(self,field): #将数字转化为枚举类型
        try:
            client = ClientTypeEnum(field.data) #尝试将收到的客户端的数字变成枚举类型 不能转变则抛出异常
        except ValueError as e:
            raise e
        self.type.data = client

class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')]) #账号
    secret = StringField(validators=[DataRequired(),Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(),Length(2,22)])

    def validate_account(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

    def validate_nickname(self,field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')

class BookSearchForm(Form):
    q = StringField(validators=[DataRequired()])
