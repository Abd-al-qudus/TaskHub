from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from api.databases import DatabaseOperation

def create_app():
    app = Flask(__name__)
    return app

app = create_app()  
app.secret_key = 'gonna change this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://taskhub_user:taskhub_user_pwd@localhost/taskhub_db' 
db = SQLAlchemy(app)
dbOps = DatabaseOperation()

from api.models import User

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
        
        db.session.add(new_user)
        db.session.commit()
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username =  request.form['username']
        password = request.form['password']
        
        db_users = dbOps.create_db_session()
        user = db_users.query(User).filter_by(username=username).first()
        if user and user.verify_password(password):
            return redirect(url_for('home'))
        
    return render_template('login.html')

@app.route('/task_manager')
def task_manager():
    return render_template('task_manager.html')


if __name__ == "__main__":
    app.run(debug=True)
