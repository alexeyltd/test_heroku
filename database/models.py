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
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='articles')
    approve_title_id = db.Column(db.Integer, unique=True, nullable=True)
    create_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.Integer, unique=False, nullable=False, default=0)
    key_words = db.Column(db.String(120), unique=False, nullable=True)
    price = db.Column(db.Integer, unique=False, nullable=True, default=None)

    @property
    def serialize(self):
        return {
            'id': self.hash_id,
            'status': self.status,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'titles': [i.serialize for i in self.titles],
            'brief': self.brief.serialize,
            'key_words': self.key_words,
            'price': self.price
        }


class Title(db.Model):
    title_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title_text = db.Column(db.String(120), unique=False, nullable=True)
    create_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    try_number = db.Column(db.Integer, unique=False, nullable=False, default=0)
    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'))
    article = db.relationship('Article', backref='titles')

    @property
    def serialize(self):
        return {
            'id': self.title_id,
            'title_text': self.title_text,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'try_number': self.try_number
        }


class Brief(db.Model):
    brief_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_type = db.Column(db.String(80), unique=False, nullable=False)
    content_length = db.Column(db.Integer, unique=False, nullable=False, default=0)
    content_language = db.Column(db.String(80), unique=False, nullable=False)
    domain = db.Column(db.String(120), unique=False, nullable=False)
    topics = db.Column(db.String(120), unique=False, nullable=False)  # todo
    competitors = db.Column(db.String(120), unique=False, nullable=True)  # todo
    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'))
    article = db.relationship('Article', backref='brief')
    create_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.title_id,
            'content_type': self.content_type,
            'create_date': self.create_date,
            'update_date': self.update_date,
            'content_length': self.content_length,
            'content_language': self.content_language,
            'domain': self.domain,
            'competitors': self.competitors,
            'topics': self.topics
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
