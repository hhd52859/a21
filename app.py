# 项目启动文件
from flask_script import Manager
from apps import create_app
from flask_migrate import Migrate,MigrateCommand
from apps.ext import db

app = create_app()
manager = Manager(app=app)
migrate = Migrate(app=app,db=db)
manager.add_command('db',MigrateCommand)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
