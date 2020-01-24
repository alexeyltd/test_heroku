from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email


# <editor-fold desc="Article">
@app.route('/api/v1/article/get', methods=['POST'])
def article_get():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/article/create', methods=['POST'])
def article_create():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/article/update', methods=['POST'])
def article_update():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/article/delete', methods=['POST'])
def article_delete():
    data = request.json
    return jsonify({'result': 'success'})

# </editor-fold>
