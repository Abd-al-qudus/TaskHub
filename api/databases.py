from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

class DatabaseOperation():
    
    def __repr__(self):
        return "class for CRUD implementation"
    
    def create_db_session(self):
        user = "taskhub_user"
        database = "taskhub_db"
        password = "taskhub_user_pwd"
        
        engine =  create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                                format(user, password, database), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        sessions = Session()
        return sessions
    
    def queryDbSession(self, object):
        session = self.create_db_session()
        new_object = session.query(object)
        return new_object
    
    def addToDbSession(self, object):
        session = self.create_db_session()
        if not isinstance(object, list):
            session.add(object)
        else:
            session.add_all(object)
        session.commit()
        
    def removeFromDbSession(self, object):
        session = self.create_db_session()
        session.delete(object)
        session.commit()
