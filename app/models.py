from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(400), nullable=True)
    image = db.Column(db.String(400), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    client = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    text = db.Column(db.Text, nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)