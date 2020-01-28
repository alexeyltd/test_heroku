from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email
from datetime import datetime


# <editor-fold desc="Article">
@app.route('/api/v1/article/get', methods=['POST'])
def article_get():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'invalid email'})

    if 'id' not in data:
        return jsonify({'result': 'success', 'data': user.serialize_full['articles']})

    articles = user.articles
    for article in articles:
        if article.hash_id == data['id']:
            return jsonify({'result': 'success', 'data': article.serialize})


@app.route('/api/v1/article/approve/title', methods=['POST'])
def article_approve_title():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'auth error'})

    article = Article.query.filter_by(hash_id=data['order_id']).first()
    if article is None:
        return jsonify({'result': 'error', 'msg': 'invalid order id'})

    # todo send notification
    if data['approve']:
        title = Title.query.get(data['title_id'])
        if title is None:
            return jsonify({'result': 'error', 'msg': 'invalid title id'})
        article.approve_title_id = data['title_id']
        article.status = 2
    else:
        article.status = 0

    article.update_date = datetime.utcnow()

    db.session.commit()

    return jsonify({'result': 'success'})


@app.route('/api/v1/article/approve/article', methods=['POST'])
def article_approve_article():
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
