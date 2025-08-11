from flask import Flask
from exts import db, moment, bootstrap
import configs


def create_app():
    app = Flask(__name__)
    app.config.from_object(configs)
    # 其他配置...
    # 动态绑定app
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    # 导入本地模块（在app初始化后）
    from models import Message

    return app


app = create_app()
import commands, views, errors
if __name__ == '__main__':

    app.run(debug=True)
