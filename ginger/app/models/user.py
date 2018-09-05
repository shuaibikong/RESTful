from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash,check_password_hash
from app.libs.error_code import NotFound,AuthFailed
from app.models.base import Base,db

class User(Base):
    id = Column(Integer,primary_key=True)
    email = Column(String(24),unique=True,nullable=False)
    nickname = Column(String(24),unique=True)
    auth = Column(SmallInteger,default=1) #权限标识
    _password = Column('password',String(100))

    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    def __getitem__(self, item):
        return getattr(self,item)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname,account,secret):
        with db.auto_commit():
            user = User() #在一个类中再调用类本身的话 应该设为类方法或静态方法
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password): #用于验证客户端登录,验证成功返回用户的id绑定token
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope' #通过用户的auth编号来确定用户权限
        return {'uid': user.id, 'scope': scope}

    def check_password(self,raw):
        if not self._password:
            return False
        return check_password_hash(self._password,raw)

