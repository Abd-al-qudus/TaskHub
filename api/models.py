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
    String)

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    description = Column(String(500), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    team_name = Column(String(80), nullable=False, unique=True)
    
    # team = relationship('Team', backref='task', cascade='all, delete')
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
    
    
# class Team(Base):
#     __tablename__ = 'team'
    
#     id = Column(Integer, primary_key=True)
#     task_title = Column(String(80), unique=True, nullable=False)
#     task_id = Column(Integer, ForeignKey('task.id'))
#     team_name = Column(String(80), nullable=False, unique=True)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(120), nullable=False)
    
    task = relationship('Task', backref='user', cascade='all, delete-orphan')

    @property
    def password(self):
        raise AttributeError('Password is not readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    