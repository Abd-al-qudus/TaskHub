from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
# from flask_login import (
#     #UserMixin,
#     LoginManager,
#     #login_user,
#     #logout_user,
#    # current_user,
#    # login_required,
# )


# def create_login_manager(): 
#     login_manager = LoginManager()
#     login_manager.session_protection = 'strong'
#     login_manager.login_view = 'login'
#     login_manager.login_message_category = 'info'
#     return login_manager

# db = SQLAlchemy()
# migrate = Migrate()
# bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    # app.secret_key = 'change-this-key'
    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # app.config['MYSQL_USER'] = 'taskhub_db_user'
    # app.config['MYSQL_PASSWORD'] = 'taskhub_db_pwd'
    # app.config['MYSQL_DB'] = 'taskhub_db'
    # app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    
    # create_login_manager().init_app(app)
    # db.init_app(app)
    # migrate.init_app(app, db)
    # bcrypt.init_app(app)
    
    return app

app = create_app()  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://taskhub_user:taskhub_user_pwd@localhost/taskhub_db' 
db = SQLAlchemy(app)

from api.models import User

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('login.html')

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
        
        user = db.Query(User).filter_by(username=username).first()
        if user and user.verify_password(password):
            return redirect(url_for('home'))
        
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
