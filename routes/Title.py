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
    brief = Brief.query.get(data['brief_id'])
    article = Article.query.filter_by(hash_id=data['article_id']).first()
    if article is None or brief is None:
        return jsonify({'result': 'error', 'msg': 'article or brief is invalid!'})
    title_data = data['title']
    title = Title(title_text=title_data['title'], keywords=title_data['keywords'],
                  meta_description=title_data['meta_description'])
    article.status = 1
    article.titles.append(title)
    db.session.commit()
    # todo send notification
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
