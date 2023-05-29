from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'taskhub_db_user'
app.config['MYSQL_PASSWORD'] = 'taskhub_db_pwd'
app.config['MYSQL_DB'] = 'taskhub_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/index')
def home():
    return "<h1> Hello there </h1>"
