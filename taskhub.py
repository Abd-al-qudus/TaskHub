from flask import Flask
from flask import render_template
# from flask_sqlalchemy import SQLAlchemy
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
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://taskhub_user:taskhub_user_pwd@localhost/taskhub'
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
@app.route('/')
def home():
    return render_template('3-feature.html')

if __name__ == "__main__":
    app.run(debug=True)