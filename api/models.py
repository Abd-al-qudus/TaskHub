from taskhub import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Task(db.Model, Base):
    __tablename__ = 'task'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    team_id = db.Column(db.String(80), db.ForeignKey('team.id'), unique=True)
    
    def __repr__(self):
        return self.title
    
class TeamMember(db.Model, Base):
    __tablename__ = 'team_member'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), unique=True, nullable=False)
    
class Team(db.Model, Base):
    __tablename__ = 'team'
    
    id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(80), unique=True, nullable=False)
    member = db.Column(db.String(80), db.ForeignKey('team_member.user_id'))
    task = relationship('Task', cascade='delete', backref='team')

class User(db.Model, Base):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    