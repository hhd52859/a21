from flask import Flask
from settings import Config
from apps.ext import db
from apps.User.view import user_bp

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)  # 配置文件
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(user_bp)

    return app