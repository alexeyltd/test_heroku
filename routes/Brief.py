from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email


# <editor-fold desc="Brief">
@app.route('/api/v1/brief/get', methods=['POST'])
def brief_get():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/brief/create', methods=['POST'])
def brief_create():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/brief/update', methods=['POST'])
def brief_update():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/brief/delete', methods=['POST'])
def brief_delete():
    data = request.json
    return jsonify({'result': 'success'})

# </editor-fold>
