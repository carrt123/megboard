from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import configs


app = Flask(__name__)
app.config.from_object(configs)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
from models import Message
import commands  # 新增这行
if __name__ == '__main__':
    app.run()