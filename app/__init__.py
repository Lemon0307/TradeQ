from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '188db0c1a734f4d4d31f26f6c0ef5562d7aa4910caeb09b2bd402a25edba2d51b4000e2245f818c9e1216cb62e3e98761ebbaac40510ce4608213ef327e32e12322f02e423'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app import routes