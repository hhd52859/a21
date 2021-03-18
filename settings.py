# 配置文件
class Config:
    DEBUG = True
    ENV = 'developement'
    # 数据库URI 需要自行修改
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://用户名:密码@localhost:端口号/数据库名?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False