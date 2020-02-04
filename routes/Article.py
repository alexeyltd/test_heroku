from app import app
from database.models import *
from flask import request, jsonify
from utils.helper import send_email
from datetime import datetime
import uuid
from Config.Config import Config


# <editor-fold desc="Article">
@app.route('/api/v1/article/get', methods=['POST'])
def article_get():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'invalid email'})

    # get all articles for user (lite)
    if 'id' not in data:
        return jsonify({'result': 'success', 'data': user.serialize_articles_lite})

    # get article by hash_id for user
    for article in user.articles:
        if article.hash_id == data['id']:
            return jsonify({'result': 'success', 'data': article.serialize})


# </editor-fold>

# <editor-fold desc="Title">
@app.route('/api/v1/title/create', methods=['POST'])
def title_create():
    data = request.json
    article = Article.query.filter_by(hash_id=data['article_id']).first()
    if article is None:
        return jsonify({'result': 'error', 'msg': 'article is invalid!'})

    if len(article.titles) >= 3:
        return jsonify({'result': 'error', 'msg': 'max number of titles exists'})

    title_data = data['title']
    title = Title(title_text=title_data['title'], keywords=title_data['keywords'],
                  meta_description=title_data['meta_description'])
    article.status = 1
    article.update_date = datetime.utcnow()
    article.titles.append(title)

    user = User.query.get(article.user_id)
    user.notifications.append(Notification(title='Title created!', text='Check new title in your orders!'))
    send_email('Title created for you and waiting for confirmation!', user.email)

    db.session.commit()
    return jsonify({'result': 'success'})


@app.route('/api/v1/article/title/approve', methods=['POST'])
def title_approve():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'auth error'})

    article = Article.query.filter_by(hash_id=data['order_id']).first()
    if article is None:
        return jsonify({'result': 'error', 'msg': 'invalid order id'})

    if data['approve']:
        title = Title.query.get(data['title_id'])
        if title is None:
            return jsonify({'result': 'error', 'msg': 'invalid title id'})
        article.approve_title_id = title.title_id
        article.titles = [title]
        article.status = 2
        send_email('New article wait you for creating!')
    else:
        if len(article.titles) >= 3:
            return jsonify({'result': 'error', 'msg': 'max number of titles exists'})
        if data['comment']:
            article.comment = data['comment']
        article.status = 0
        send_email('Renew title wait you for creating!')

    article.update_date = datetime.utcnow()
    db.session.commit()
    return jsonify({'result': 'success'})


# </editor-fold>

# <editor-fold desc="ArticleContent">
@app.route('/api/v1/content/create', methods=['POST'])
def content_create():
    data = request.form
    img = request.files['img']

    article = Article.query.filter_by(hash_id=data['article_id']).first()
    if article is None:
        return jsonify({'result': 'error', 'msg': 'invalid article id'})

    if len(article.contents) >= 3:
        return jsonify({'result': 'error', 'msg': 'max number of contents exists'})

    content = ArticleContent(text=bytearray(data['text'], encoding='utf-8'),
                             img=img.read())
    article.contents.append(content)
    if len(article.contents) == 3:
        article.status = 6
        article.approve_content_id = content.content_id
    else:
        article.status = 5
    article.update_date = datetime.utcnow()

    user = User.query.get(article.user_id)
    user.notifications.append(Notification(title='Content created!', text='Check new article in your orders!'))
    send_email('Content created for your article and waiting for you!', user.email)

    db.session.commit()
    return jsonify({'result': 'success'})


@app.route('/api/v1/article/content/approve', methods=['POST'])
def content_approve():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'result': 'error', 'msg': 'auth error'})

    article = Article.query.filter_by(hash_id=data['order_id']).first()
    if article is None:
        return jsonify({'result': 'error', 'msg': 'invalid order id'})

    if data['approve']:
        content = ArticleContent.query.get(data['content_id'])
        if content is None:
            return jsonify({'result': 'error', 'msg': 'invalid content id'})
        article.approve_content_id = data['content_id']
        article.status = 6
        for content in article.contents:
            if content.content_id == article.approve_content_id:
                article.contents = [content]
                break
        for title in article.titles:
            if title.title_id == article.approve_title_id:
                article.titles = [title]
                break
        send_email('Article accepted!')
    else:
        if len(article.contents) >= 3:
            return jsonify({'result': 'error', 'msg': 'max number of contents exists'})
        if data['comment']:
            article.comment = data['comment']
        article.status = 2
        send_email('Need to recreate article!')

    article.update_date = datetime.utcnow()
    db.session.commit()
    return jsonify({'result': 'success'})


# </editor-fold>

# <editor-fold desc="Brief">
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


# </editor-fold>

# <editor-fold desc="Image">
@app.route('/api/v1/img/get/<string:article_id>', methods=['GET'])
def img_get(article_id):
    article = Article.query.filter_by(hash_id=article_id).first()
    if article is None:
        return jsonify({'result': 'error', 'msg': 'invalid order id'})

    content = article.contents[0].img
    return app.response_class(content, mimetype='application/octet-stream')
# </editor-fold>
