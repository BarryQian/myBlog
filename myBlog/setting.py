# _*_ coding: utf-8 _*_

#调用模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'  #这个有什么要求

#mysql数据库连接
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/blogUser"