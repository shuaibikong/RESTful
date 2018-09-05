from enum import Enum

class ClientTypeEnum(Enum): #枚举类型 如果传入的值符合 则赋给变量 对应的属性 否则抛出异常
    USER_EMAIL = 100
    USER_MOBILE = 101

    USER_MINA = 200
    USER_WX = 201