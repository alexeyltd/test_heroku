from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email


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
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'Invalid email'})
    user.notifications.append(Notification(title=data['notification']['title'], text=data['notification']['text']))
    if data['notification']['send_email_status']:
        send_email(data['notification']['title'] + ': ' + data['notification']['text'], data['email'])
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
