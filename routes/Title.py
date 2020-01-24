from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email


# <editor-fold desc="Title">
@app.route('/api/v1/title/get', methods=['POST'])
def title_get():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/title/create', methods=['POST'])
def title_create():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/title/update', methods=['POST'])
def title_update():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/title/delete', methods=['POST'])
def title_delete():
    data = request.json
    return jsonify({'result': 'success'})

# </editor-fold>
