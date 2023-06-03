from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

def create_db_session():
    user = "taskhub_user"
    database = "taskhub_db"
    password = "taskhub_user_pwd"
    
    engine =  create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                            format(user, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    sessions = Session()
    return sessions
