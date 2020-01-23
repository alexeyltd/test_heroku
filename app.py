from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_migrate import Migrate

from werkzeug.security import generate_password_hash
import uuid

from Config.Config import Config
from utils.helper import generate_code, send_email

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='static')

# main app config
app.config.from_object(Config)

# db init
db = SQLAlchemy(app)
db.create_all()
db.session.commit()
migrate = Migrate(app, db)

from database.models import User, Article, Notification


# <editor-fold desc="Admin">
@app.route('/api/v1/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    if data['email'] != 'admin' or data['password'] != '123':
        return jsonify({'result': 'error', 'msg': 'invalid credentials'})
    result = []
    users = User.query.all()
    for user in users:
        result.append(user.serialize_full)
    return jsonify({'result': 'success', 'data': result})


# </editor-fold >

# <editor-fold desc="Account">
@app.route('/api/v1/account/login', methods=['POST'])
def account_login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None or not user.check_password(data['password']):
        return jsonify({'result': 'error', 'msg': 'invalid credentials'})
    return jsonify({'result': 'success', 'user': user.serialize, 'token': 'token123'})


@app.route('/api/v1/account/registration', methods=['POST'])
def account_registration():
    try:
        code = generate_code(4)
        data = request.json
        if 'business_name' in data:
            b_name = data['business_name']
        else:
            b_name = None
        user = User(first_name=data['first_name'], last_name=data['last_name'], email=data['email'],
                    password_hash=generate_password_hash(data['password']), business_name=b_name,
                    confirm_status=code, token=uuid.uuid1())
        send_email(str(code), data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'result': 'success', 'user': user.serialize, 'token': user.token})
    except exc.IntegrityError:
        return jsonify({'result': 'error', 'msg': 'email already exist'})


@app.route('/api/v1/account/confirm', methods=['POST'])
def account_confirm_registration():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'invalid credentials'})
    if user.confirm_status == int(data['code']):
        user.confirm_status = 1
        db.session.commit()
        return jsonify({'result': 'success'})
    return jsonify({'result': 'error', 'msg': 'invalid code'})


@app.route('/api/v1/account/update', methods=['POST'])
def account_update():
    return jsonify({'result': 'success'})


# </editor-fold>

# <editor-fold desc="Article">
@app.route('/api/v1/article/get', methods=['POST'])
def article_get():
    return jsonify({'result': 'success'})


@app.route('/api/v1/article/create', methods=['POST'])
def article_create():
    data = request.json

    return jsonify({'result': 'success'})


@app.route('/api/v1/article/update', methods=['POST'])
def article_update():
    return jsonify({'result': 'success'})


@app.route('/api/v1/article/delete', methods=['POST'])
def article_delete():
    return jsonify({'result': 'success'})


# </editor-fold>

# <editor-fold desc="Notification">
@app.route('/api/v1/notification/get', methods=['POST'])
def notification_get():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'Invalid email'})
    return jsonify({'result': 'success', 'data': user.serialize_full['notifications']})


@app.route('/api/v1/notification/create', methods=['POST'])
def notification_create():
    data = request.json
    # todo auth check
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'Invalid email'})
    user.notifications.append(Notification(title=data['notification']['title'], text=data['notification']['text']))
    db.session.commit()
    return jsonify({'result': 'success'})


@app.route('/api/v1/notification/update', methods=['POST'])
def notification_update():
    data = request.json
    notification = Notification.query.get(data['id'])
    if notification is None:
        return jsonify({'result': 'error', 'msg': 'Invalid id'})
    notification.is_checked = data['is_checked']
    db.session.commit()
    return jsonify({'result': 'success'})


@app.route('/api/v1/notification/delete', methods=['POST'])
def notification_delete():
    data = request.json
    notification = Notification.query.get(data['id'])
    if notification is None:
        return jsonify({'result': 'error', 'msg': 'Invalid id'})
    db.session.delete(notification)
    db.session.commit()
    return jsonify({'result': 'success'})


# </editor-fold>

# frontend index page
@app.route('/')
def index():
    return render_template('index.html')


# all to vue router
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
