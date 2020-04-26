# core/views.py
# from puppycompanyblog.models import BlogPost
from flask import render_template,request,Blueprint
from puppycompanyblog import db, default_sensorData
from puppycompanyblog.models import SensorData
import time

core = Blueprint('core',__name__)

@core.route('/')
def index():
    # page = request.args.get('page',1,type=int)
    # blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    # return render_template('index.html',blog_posts=blog_posts)
    db_s, db_ms = divmod(db.child("moisture/Timestamp_current").get().val(), 1000)

    default_sensorData.time=time.ctime(db_s)
    default_sensorData.sensor_1=db.child("moisture/sensor_1_current").get().val()
    default_sensorData.sensor_2=db.child("moisture/sensor_2_current").get().val()
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Local time:", local_time)
    # db_s, db_ms = divmod(default_sensorData.time, 1000)
    # print(time.ctime(db_s))
    # print("Local time:", local_time)

    return render_template('home.html',sensorData=default_sensorData)

@core.route('/info')
def info():
    return render_template('info.html')
