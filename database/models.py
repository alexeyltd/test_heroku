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
            # 'articles': [i.serialize for i in self.articles],
            'notifications': count
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
            'notifications': [i.serialize for i in self.notifications]
        }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {} {} {}>'.format(self.email, self.first_name, self.last_name)


class Article(db.Model):
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hash_id = db.Column(db.String(120), index=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='articles')
    title = db.Column(db.String(80), unique=False, nullable=False)
    create_date_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.Integer, unique=False, nullable=False, default=0)
    key_words = db.Column(db.String(120), unique=False, nullable=True)

    # todo file_name = db.Column(db.String(120), unique=True, nullable=True)

    @property
    def serialize(self):
        return {
            'id': self.hash_id,
            'title': self.title,
            'status': self.status,
            'date': self.create_date_timestamp
        }

    def __repr__(self):
        return '<Article {} {}>'.format(self.user_id, self.title)


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

    def __repr__(self):
        return '<Notification {} {} {}>'.format(self.user_id, self.title, self.text)
