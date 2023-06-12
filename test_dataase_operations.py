import unittest
from api.databases import (
    DatabaseOperation,
    TeamMemberDatabaseOperation,
    UserDatabaseOperation,
    TaskDatabaseOperation,
) 
from taskhub import (
    db, 
    app,
)
from api.models import (
    User,
    TeamMember,
    Task,
)

class TestDatabaseOperation(unittest.TestCase):
    """test the database class"""
    SQL_ALCHEMY_URI = 'mysql+mysqldb://taskhub_user:taskhub_user_pwd@localhost/taskhub_db' 
    TESTING = True
    userDb = UserDatabaseOperation()
    
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = self.SQL_ALCHEMY_URI
        return app
    
    def setUp(self):
        """initialize the app context for database creation"""
        with app.app_context():
            db.create_all()
        
    def tearDown(self):
        """remove all initialized context"""
        with app.app_context():
            db.session.remove()
            db.drop_all()
        
    def test_add_to_db_session(self):
        """test insert operations on the database"""
        user = User(username="anewuser")
        user.password = "test"
        with self.assertRaises(Exception):
            self.userDb.add_user(user=user)
            saved = self.userDb.get_user(usrname=user.username)
            self.assertIsNotNone(saved)
            self.assertEqual(saved.username, "anewuser")
        
        # duplicate transaction
        user = User(username="jck{}{}[]")
        with self.assertRaises(Exception):
            user.password = 2
            self.userDb.add_user(user=user)
            saved = self.userDb.get_user(usrname=user.username)
            self.assertIsNotNone(saved)
            self.assertEqual(saved.username, "testers")
        
        # what if username is empty
        user = User(username="")
        user.password = "test"
        with self.assertRaises(Exception):
            self.userDb.add_user(user=user)
            saved = self.userDb.get_user(usrname=user.username)
            self.assertIsNotNone(saved)
            self.assertEqual(saved.username, "")
        
        #what if username is not a string
        user = User(username=2)
        user.password = ""
        with self.assertRaises(Exception):
            self.userDb.add_user(user=user)
            saved = self.userDb.get_user(usrname=user.username)
            self.assertIsNotNone(saved)
            self.assertEqual(saved.username, 2)
        
        user = User(username=[])
        user.password = "test"
        with self.assertRaises(Exception):
            self.userDb.add_user(user=user)
            saved = self.userDb.get_user(usrname=user.username)
            print(saved)
            self.assertIsNotNone(saved)
            self.assertEqual(saved.username, [])
        
        user = User(username=None)
        user.password = "test"
        with self.assertRaises(Exception):
            self.userDb.add_user(user=user)
            saved = self.userDb.get_user(usrname=user.username)
            self.assertIsNotNone(saved)
            self.assertEqual(saved.username, None)
            
    def test_get_from_db_session(self):
        """test fetch operations from the database"""
        # fetch users without arguments or usrname=""
        with self.assertRaises(Exception):
            user = self.userDb.get_user()
            self.assertIsNotNone(user)
        
        # fetch a particular user
        with self.assertRaises(Exception):
            user = self.userDb.get_user(usrname="engineer")
            self.assertIsNotNone(user)
            
        # fetch a user that does not exist
        with self.assertRaises(Exception):
            user = self.userDb.get_user(usrname="bad man fist")
            self.assertIsNone(user)
        
        
if __name__ == "__main__":
    unittest.main()
