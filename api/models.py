from taskhub import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
# from flask_login import UserMixin
# from sqlalchemy import Column, String, Integer

class Task(db.Model):
    __tablename__ = 'task'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    team_id = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return self.title

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    
    @property
    def password(self):
        raise AttributeError('Password is nor readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    