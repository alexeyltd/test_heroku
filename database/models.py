from app import db
import psycopg2
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(120), unique=False, nullable=False)
    business_name = db.Column(db.String(120), unique=False, nullable=True)
    confirm_status = db.Column(db.Integer, unique=False, nullable=False)
    role_admin = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    token = db.Column(db.String(80), unique=True, nullable=False)

    @property
    def serialize(self):
        status = 1
        if self.confirm_status != 1:
            status = 0
        count = 0
        for i in self.notifications:
            if not i.is_checked:
                count += 1
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'business_name': self.business_name,
            'confirm_status': status,
            'notifications': count,
            'role_admin': self.role_admin
        }

    @property
    def serialize_full(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'business_name': self.business_name,
            'confirm_status': self.confirm_status,
            'articles': [i.serialize for i in self.articles],
            'notifications': [i.serialize for i in self.notifications],
            'role_admin': self.role_admin
        }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Article(db.Model):
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    hash_id = db.Column(db.String(120), index=True, unique=True, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=True, default=None)
    approve_title_id = db.Column(db.Integer, unique=True, nullable=True)
    approve_content_id = db.Column(db.Integer, unique=True, nullable=True)
    status = db.Column(db.Integer, unique=False, nullable=False, default=0)
    # 0=need to create title, 1=need to approve title,
    # 2,[3,4] need to create article, 5=need to approve article, 6=complete
    # 3,4 now removed
    comment = db.Column(db.String(200), unique=False, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='articles')
    create_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.hash_id,
            'status': self.status,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'titles': [i.serialize for i in self.titles],
            'brief': [i.serialize for i in self.brief],
            'contents': [i.serialize for i in self.contents],
            'price': self.price,
            'approve_title_id': self.approve_title_id,
            'approve_content_id': self.approve_content_id,
            'comment': self.comment
        }


class Title(db.Model):
    title_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title_text = db.Column(db.String(120), unique=False, nullable=True)
    keywords = db.Column(db.String(120), unique=False, nullable=True)
    meta_description = db.Column(db.String(250), unique=False, nullable=True)

    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'))
    article = db.relationship('Article', backref='titles')
    create_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.title_id,
            'title_text': self.title_text,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'keywords': self.keywords,
            'meta_description': self.meta_description
        }


class Brief(db.Model):
    brief_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    content_type = db.Column(db.String(80), unique=False, nullable=False)
    content_length = db.Column(db.Integer, unique=False, nullable=False, default=0)
    content_language = db.Column(db.String(80), unique=False, nullable=False)
    current_domain_url = db.Column(db.String(120), unique=False, nullable=True)
    topic_suggestions = db.Column(db.String(120), unique=False, nullable=True)
    intended_result = db.Column(db.String(120), unique=False, nullable=True)
    suggested_keywords = db.Column(db.String(120), unique=False, nullable=True)
    specific_requests = db.Column(db.String(120), unique=False, nullable=True)
    competitors = db.Column(db.String(120), unique=False, nullable=True)
    target_customer = db.Column(db.String(120), unique=False, nullable=True)

    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'))
    article = db.relationship('Article', backref='brief', uselist=False)
    create_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.brief_id,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'content_type': self.content_type,
            'content_length': self.content_length,
            'content_language': self.content_language,
            'current_domain_url': self.current_domain_url,
            'competitors': self.competitors,
            'topic_suggestions': self.topic_suggestions,
            'intended_result': self.intended_result,
            'suggested_keywords': self.suggested_keywords,
            'specific_requests': self.specific_requests,
            'target_customer': self.target_customer
        }


class ArticleContent(db.Model):
    content_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    text = db.Column(db.LargeBinary, nullable=False)
    img = db.Column(db.String(120), nullable=False)

    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'))
    article = db.relationship('Article', backref='contents')
    create_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.content_id,
            'create_date': self.create_date,
            'text': self.text.decode("utf-8"),
            'img': self.img
        }


class Notification(db.Model):
    notification_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='notifications')
    title = db.Column(db.String(80), unique=False, nullable=False)
    create_date_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_checked = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    text = db.Column(db.String(120), unique=False, nullable=True)

    @property
    def serialize(self):
        return {
            'title': self.title,
            'is_checked': self.is_checked,
            'date': self.create_date_timestamp,
            'text': self.text,
            'notification_id': self.notification_id
        }
