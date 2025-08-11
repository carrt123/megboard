from flask import Flask
from exts import db, moment, bootstrap
import configs
from views import view


def create_app():
    app = Flask(__name__)
    app.config.from_object(configs)
    # 动态绑定app
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    from models import Message

    return app


app = create_app()
app.register_blueprint(view)
import errors, commands

if __name__ == '__main__':
    app.run(debug=True)
