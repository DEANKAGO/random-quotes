from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class BaseModel():
    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    isWritter = db.Column(db.Boolean(), default=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def create(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Blog(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    blog = db.Column(db.String(1000), nullable=False)
    timestamp = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, blog, timestamp, user_id):
        self.title = title
        self.blog = blog
        self.timestamp = timestamp
        self.user_id = user_id

    def __repr__(self):
        return '<Blog: {}>'.format(self.id)