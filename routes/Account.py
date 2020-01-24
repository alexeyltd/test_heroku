from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email, generate_code
import uuid
from sqlalchemy import exc


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
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None or not user.check_password(data['password']):
        return jsonify({'result': 'error', 'msg': 'invalid credentials'})
    # todo update user data's
    db.session.commit()
    return jsonify({'result': 'success', 'user': user.serialize, 'token': 'token123'})


@app.route('/api/v1/account/recovery', methods=['POST'])
def account_recovery():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'invalid email'})
    tmp_pass = str(uuid.uuid1())
    send_email(tmp_pass, data['email'])
    user.password_hash = generate_password_hash(tmp_pass)
    db.session.commit()
    return jsonify({'result': 'success'})

# </editor-fold>
