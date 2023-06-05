from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from api.models import (
    User,
    Task,
    TeamMember,
    )

class DatabaseOperation:
    """perform CRUD operation on the database"""
    
    def __repr__(self):
        return "class for CRUD implementation"
    
    def create_db_session(self):
        """create a database connection"""
        user = "taskhub_user"
        database = "taskhub_db"
        password = "taskhub_user_pwd"
        
        engine =  create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                                format(user, password, database), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        sessions = Session()
        return sessions
    
    def queryDbSession(self, object):
        """query the connection based on object"""
        if object:
            session = self.create_db_session()
            new_object = session.query(object)
            return new_object
    
    def addToDbSession(self, object):
        """add object to db session"""
        if object:
            session = self.create_db_session()
            if not isinstance(object, list):
                session.add(object)
            else:
                session.add_all(object)
            session.commit()
        
    def removeFromDbSession(self, object):
        """remove object from db seesion"""
        if object:
            session = self.create_db_session()
            session.delete(object)
            session.commit()

class UserDatabaseOperation(User, DatabaseOperation):
    """perform CRUD operation on the database for user model"""
    
    init_db = DatabaseOperation()
    init_user_db = init_db.queryDbSession(User)
    
    def get_users(self, usrname=""):
        """get all users from the database"""
        if usrname != "":
            return self.init_user_db.filter_by(username=User.username).all()
        else:
            return self.init_user_db.filter_by(username=User.username). \
                filter(usrname == User.username).first()
    
    def delete_user(self, username=""):
        """delete a user in the database"""
        if username != "":
            user = self.get_users(usrname=username)
        else:
            user = self.get_users()
        self.init_db.removeFromDbSession(user)
            
    def add_user(self, user):
        if user:
            self.init_db.addToDbSession(user)
        
class TaskdatabaseOperation(DatabaseOperation, Task):
    """perform CRUD operation on the database for task model"""
    
    init_db = DatabaseOperation()
    init_task_db = init_db.queryDbSession(Task)
    task_session = init_db.create_db_session()
    
    def get_task(self, task_title=""):
        "fetch user tasks from the db"
        if task_title != "":
            return self.init_task_db.filter_by(title=task_title).all()
        else:
            return self.init_task_db.filter_by(title=task_title).\
                filter(Task.title == task_title).first()
    
    def add_new_task(self, task):
        """add new task to the database"""
        if task:
            self.init_db.addToDbSession(task)
            
    def delete_task(self, task_id):
        """delete a task with task id"""
        if task_id:
            task = self.init_task_db.get(task_id)
            self.init_db.removeFromDbSession(task)
        
    def edit_task(self, task_id, **kwargs):
        """edit task with task id"""
        if task_id:
            task = self.init_task_db.get(task_id)
            task.title = kwargs.get('title')
            task.description = kwargs.get('description')
            self.task_session.commit()

class Team(DatabaseOperation, TeamMember):
    """perform CRUD operation on the database for team model"""
    
    init_db = DatabaseOperation()
    init_team_db = init_db.queryDbSession(TeamMember)
    
        