# _*_ coding: utf-8 _*_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myBlog.controller import blog_message

#创建项目对象
app = Flask(__name__)
#数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/bloguser'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = '123456'  #要用到flash消息闪现，要设置SERET_KEY,值任意
#创建数据库对象
db = SQLAlchemy(app)