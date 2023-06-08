from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from api.databases import DatabaseOperation, UserDatabaseOperation
from api.forms import login_form, register_form
from api.models import User
from flask_login import (
    UserMixin, 
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'gonna change this'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://taskhub_user:taskhub_user_pwd@localhost/taskhub_db' 
    login_manager.init_app(app=app)
    bcrypt.init_app(app=app)
    
    return app

app = create_app()  
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)


dbOps = DatabaseOperation()
userDb = UserDatabaseOperation()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = register_form()
    if form.validate_on_submit():
        email = form.email.data
        pwd = form.pwd.data
        username = form.username.data
        new_user = User(username=username, email=email)
        new_user.password = pwd
        userDb.add_user(new_user)
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = login_form()
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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(debug=True)
