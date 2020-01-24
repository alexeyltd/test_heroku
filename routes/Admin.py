from app import app
from database.models import *
from flask import request, jsonify


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
