from flask import Flask
from exts import db, bootstrap, moment
import configs

app = Flask(__name__)
app.config.from_object(configs)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db.init_app(app)
bootstrap.init_app(app)
moment.init_app(app)

app.run()