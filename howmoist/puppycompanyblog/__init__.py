# puppycompanyblog/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'mysecret'


###################################
### DATABASE SETUP ################
###################################
import pyrebase
from dotenv import load_dotenv
load_dotenv()  # evaluates to true
config = {
  "apiKey": os.environ['FIREBASE_API_KEY'],
  "authDomain": "esp32-garden.firebaseapp.com",
  "databaseURL": "https://esp32-garden.firebaseio.com",
  "storageBucket": "esp32-garden.appspot.com",
  "serviceAccount": "serviceAccountCredentials.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app) # firebase.database()
# Migrate(app,db)
beerTable = []

###################################
### LOGIN CONFIGS #################
###################################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

###### SETUP BLUEPRINT ###################
from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
# from puppycompanyblog.blog_posts.views import blog_posts
from puppycompanyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(users)
# app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)

#########################################
# flask db init
# flask db migrate -m "first migration"
# flask db upgrade
