from sqlalchemy.orm import (
    sessionmaker
    )
from sqlalchemy import (
    create_engine, 
    )
from api.models import (
    User,
    Task,
    TeamMember,
    Base
    )


user = "taskhub_user"
database = "taskhub_db"
password = "taskhub_user_pwd"
    
engine =  create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                        format(user, password, database), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sessions = Session()


class DatabaseOperation:
    """perform CRUD operation on the database"""
    
    def __repr__(self):
        return "class for CRUD implementation"
    
    def create_db_session(self):
        """create a database connection"""
        return sessions
    
    def query_db_session(self, object):
        """query the connection based on object"""
        if object:
            session = self.create_db_session()
            new_object = session.query(object)
            return new_object
    
    def add_to_db_session(self, object):
        """add object to db session"""
        if object:
            session = self.create_db_session()
            if not isinstance(object, list):
                session.add(object)
            else:
                session.add_all(object)
            session.commit()
        
    def remove_from_db_session(self, object):
        """remove object from db seesion"""
        if object:
            session = self.create_db_session()
            session.delete(object)
            session.commit()

class UserDatabaseOperation(User, DatabaseOperation):
    """perform CRUD operation on the database for user model"""
    
    init_db = DatabaseOperation()
    init_user_db = init_db.query_db_session(User)
    
    def get_user(self, usrname=""):
        """get all users from the database"""
        if not isinstance(usrname, str):
            raise ValueError("Username must be a string")
        else:
            if usrname == "":
                return self.init_user_db.filter_by(username=User.username).all()
            else:
                return self.init_user_db.filter_by(username=User.username). \
                    filter(usrname == User.username).first()
    
    def delete_user(self, username):
        """delete a user in the database"""
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        else:
            if username:
                user = self.get_user(usrname=username)
                self.init_db.remove_from_db_session(user)
            
    def add_user(self, user):
        if user:
            self.init_db.add_to_db_session(user)
        
class TaskDatabaseOperation(DatabaseOperation, Task):
    """perform CRUD operation on the database for task model"""
    
    init_db = DatabaseOperation()
    init_task_db = init_db.query_db_session(Task)
    task_session = init_db.create_db_session()
    
    def get_task(self, task_title=""):
        "fetch user tasks from the db"
        if not isinstance(task_title, str):
            raise ValueError("Task title must be a string")
        else:
            if task_title == "":
                return self.init_task_db.filter_by(title=Task.title).all()
            else:
                return self.init_task_db.filter_by(title=task_title).\
                    filter(Task.title == task_title).first()
    
    def add_new_task(self, task):
        """add new task to the database"""
        if task:
            self.init_db.add_to_db_session(task)
            
    def delete_task(self, task_title=""):
        """delete a task with task id"""
        if not isinstance(task_title, str):
            raise ValueError("Task title must be a string")
        else:
            if task_title:
                task = self.get_task(task_title=task_title)
                self.init_db.remove_from_db_session(task)
        
    def edit_task(self, task_title="", **kwargs):
        """edit task with task id"""
        if not isinstance(task_title, str) or kwargs:
            raise ValueError("function arguments must be <str> <dict>")
        else:
            if task_title:
                task = self.get_task(task_title=task_title)
                task.title = kwargs.get('title')
                task.description = kwargs.get('description')
                self.task_session.commit()

class TeamMemberDatabaseOperation(DatabaseOperation, TeamMember):
    """perform CRUD operation on the database for team member model"""
    
    init_db = DatabaseOperation()
    init_team_db = init_db.query_db_session(TeamMember)
    
    def get_team_member(self, user_id=None, task_id=None, team_name="", task_name=""):
        """fetche team members in the database"""
        if not isinstance((team_name, task_name), (str, str)):
            raise ValueError("arguments must strictly be strings")
        else:
            if team_name == "" and task_name == "":
                return self.init_team_db.filter_by(team_name=TeamMember.team_name).all()
            else:
                return self.init_team_db.filter_by(team_name=TeamMember.team_name).\
                                                    filter(TeamMember.task_id == task_id and
                                                        TeamMember.user_id == user_id and 
                                                        TeamMember.task_name == task_name).first()
        
    def add_new_team_member(self, team_member):
        """add a new team member"""
        if team_member:
            self.init_db.add_to_db_session(team_member)
            
    def delete_team_member(self, team_member):
        """delete the team member"""
        if team_member:
            self.init_db.remove_from_db_session(team_member)
    