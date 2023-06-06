from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.databases import DatabaseOperation, UserDatabaseOperation
from api.models import User

def create_app():
    app = Flask(__name__)
    return app

app = create_app()  
app.secret_key = 'gonna change this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://taskhub_user:taskhub_user_pwd@localhost/taskhub_db' 
db = SQLAlchemy(app)
migrate = Migrate(app, db)
dbOps = DatabaseOperation()
userDb = UserDatabaseOperation()

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        new_user = User(username=username)
        new_user.password = password
        
        userDb.add_user(new_user)
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username =  request.form['username']
        password = request.form['password']
        
        user = userDb.get_user(usrname=username)
        if user and user.verify_password(password):
            return redirect(url_for('home'))
        
    return render_template('login.html')

@app.route('/task_manager')
def task_manager():
    return render_template('task_manager.html')

@app.route('/admin')
def admin():
    get_all_users = UserDatabaseOperation().get_user()
    return render_template('admin.html', users=get_all_users)


if __name__ == "__main__":
    app.run(debug=True)
