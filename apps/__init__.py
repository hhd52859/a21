from flask import Flask
from settings import Config
from apps.ext import db
from apps.User.view import user_bp
from apps.Alarm.view import alarm_bp
from apps.Device.view import device_bp
from apps.Inspect.view import inspect_bp
from apps.System.view import system_bp
from apps.Monitor.view import monitor_bp
from apps.Overview.view import overview_bp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)  # 配置文件
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(alarm_bp)
    app.register_blueprint(device_bp)
    app.register_blueprint(inspect_bp)
    app.register_blueprint(system_bp)
    app.register_blueprint(monitor_bp)
    app.register_blueprint(overview_bp)
    return app
