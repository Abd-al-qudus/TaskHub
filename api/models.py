from taskhub import db
# from flask_login import UserMixin
# from sqlalchemy import Column, String, Integer

class Task(db.Model):
    __tablename__ = 'Task'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    team_id = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self) -> str:
        return "<Task %r" %self.title
