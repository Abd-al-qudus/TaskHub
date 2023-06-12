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
    
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = self.SQL_ALCHEMY_URI
        return app
    
    def setUp(self):
        with app.app_context():
            db.create_all()
        
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
        
    def test_add_to_db_session(self):
        user = User(username="testers")
        user.password = "test"
        UserDatabaseOperation().add_user(user=user)
        
        saved = UserDatabaseOperation().get_user(usrname=user.username)
        self.assertIsNotNone(saved)
        self.assertEqual(saved.username, "testers")
        
        
if __name__ == "__main__":
    unittest.main()
