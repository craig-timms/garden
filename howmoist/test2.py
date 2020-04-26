import os
# from puppycompanyblog.models import SensorData

class SensorData():
    user_id = 'default'
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

default_sensorData = SensorData(user_id="T8TkHy1Vy2fC5FyoJxma4pjCyMi2",
                     time=0,
                     sensor_1=100,
                     sensor_2=100      )

print(default_sensorData.user_id)
# id = db.child("moisture/sensor_1_current").get().val()
sensor_1_data = db.child("moisture/sensor_1_current").get().val()
print(sensor_1_data)
