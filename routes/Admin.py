from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email


# <editor-fold desc="Admin">
@app.route('/api/v1/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    if data['email'] != 'admin' or data['password'] != '123':
        return jsonify({'result': 'error', 'msg': 'invalid credentials'})
    result = []
    users = User.query.all()
    for user in users:
        result.append(user.serialize_contents_lite)
    return jsonify({'result': 'success', 'data': result})


@app.route('/api/v1/admin/message/create', methods=['POST'])
def admin_create_message():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'invalid credentials'})
    send_email('msg: ' + data['message'] + ' from: ' + data['email'])
    return jsonify({'result': 'success'})

# </editor-fold >
