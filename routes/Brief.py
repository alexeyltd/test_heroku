from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email
import uuid
from Config.Config import Config


# <editor-fold desc="Brief">
@app.route('/api/v1/brief/get', methods=['POST'])
def brief_get():
    data = request.json
    return jsonify({'result': 'success'})


@app.route('/api/v1/brief/create', methods=['POST'])
def brief_create():
    data = request.json
    brief_data = data['brief']
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'invalid email'})
    brief = Brief(content_type=brief_data['content_type'], content_length=brief_data['content_length'],
                  content_language=brief_data['content_language'], current_domain_url=brief_data['current_domain_url'],
                  topic_suggestions=brief_data['topic_suggestions'], intended_result=brief_data['intended_result'],
                  suggested_keywords=brief_data['suggested_keywords'], specific_requests=brief_data['specific_request'],
                  competitors=brief_data['competitors'], target_customer=brief_data['target_customer'])

    article = Article(hash_id=str(uuid.uuid1()), price=int(brief.content_length) * Config.koef)
    article.brief.append(brief)
    user.articles.append(article)
    db.session.commit()
    send_email('New brief wait you!')
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
