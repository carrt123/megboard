from flask import flash, redirect, url_for, render_template
from manage import app
from models import Message
from exts import db
from forms import MessageForm
import bleach

ALLOWED_TAGS = ['b', 'i', 'em', 'strong', 'p']
ALLOWED_ATTRIBUTES = {}


@app.route('/', methods=["GET", "POST"])
def index():  # 主页
    form = MessageForm()
    if form.validate_on_submit():
        try:  # 捕获数据异常
            name = form.name.data.strip()
            body = form.body.data.strip()
            if not name or not body:
                flash('Name and message cannot be empty!', 'error')
                return redirect(url_for('index'))

            message = Message(body=body, name=name)
            db.session.add(message)
            db.session.commit()
            flash('Your message have been set to the world!')
        except Exception as e:
            db.session.rollback()
            flash(f'Failed to save message: {str(e)}', 'error')
        return redirect((url_for('index')))
    messages = Message.query.order_by(Message.timestamp.desc()).limit(100).all()
    return render_template('index.html', form=form, message=messages)
