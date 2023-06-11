from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, 
    Integer, 
    ForeignKey, 
    String,
    Boolean)

from flask_login import UserMixin

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    description = Column(String(500), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    team_name = Column(String(80), nullable=False, unique=True)
    status = Column(Boolean, nullable=False)
    
    team_member = relationship('TeamMember', backref='task', cascade='all, delete')
    
    def __repr__(self):
        return self.title
    
class TeamMember(Base):
    __tablename__ = 'team_member'
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('task.id'))
    user_id = Column(Integer, nullable=False)
    team_name = Column(String(120), nullable=False)
    task_name = Column(String(120), nullable=False)
    
    def __repr__(self):
        return self.task_name
    

class User(UserMixin, Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(200), nullable=False)
    
    task = relationship('Task', backref='user', cascade='all, delete-orphan')

    @property
    def password(self):
        raise AttributeError('Password is not readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return self.username
    