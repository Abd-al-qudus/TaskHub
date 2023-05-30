# from taskhub import db
# from flask_login import UserMixin
# from sqlalchemy import Column, String, Integer

# class User(UserMixin, db.Model):
#     __tablename__ = 'user'
    
#     id = Column(Integer, primary_key=True)
#     username = Column(String(80), unique=True, nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     password = Column(String(120), unique=True, nullable=False)
    
#     def __repr__(self) -> str:
#         return "<User %r" %self.username
