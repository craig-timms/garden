#models.py
# from puppycompanyblog import login_manager
# from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
import itertools

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# class User(db.Model,UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key=True)
#     profile_image = db.Column(db.String(64),nullable=False,
#                                 default='default_profile.png')
#     email = db.Column(db.String(64),unique=True,index=True)
#     username = db.Column(db.String(64),unique=True,index=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('BlogPost',backref='author',lazy=True)
#     def __init__(self,email,username,password):
#         self.email = email
#         self.username = username
#         self.password_hash = generate_password_hash(password)
#     def check_password(self,password):
#         return check_password_hash(self.password_hash,password)
#     def __repr__(self):
#         return f"Username {self.username}"
#
class SensorData():
    user_id = 1
    time = 0
    sensor_1 = 100
    sensor_2 = 100
    # users = db.relationship(User)
    # id = db.Column(db.Integer,primary_key=True)
    # user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    # date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    # title = db.Column(db.String(140),nullable=False)
    # text = db.Column(db.Text,nullable=False)
    def __init__(self,user_id,time,sensor_1,sensor_2):
        self.user_id = user_id
        self.time = time
        self.sensor_1 = sensor_1
        self.sensor_2 = sensor_2
    def __repr__(self):
        return f"ID: {self.user_id} -- Time: {self.time} --- {self.sensor_1} --- {self.sensor_2}"

# class BeerEntry:
#     class_counter= 1
#     def __init__(self,man,model,alc,volume,quantity,price):
#         self.man = man
#         self.model = model
#         self.alc = float(alc)
#         self.volume = float(volume)
#         self.quantity = float(quantity)
#         self.price = float(price)
#         self.eff = int(self.alc*self.volume/(self.price/self.quantity))
#         self.id= BeerEntry.class_counter
#         BeerEntry.class_counter += 1
#     def __del__(self):
#         print('deleted')
