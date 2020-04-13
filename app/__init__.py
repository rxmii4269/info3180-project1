from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import sha3_512
from os import urandom


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd548eac0f34844a63d85def9c8e3c86587d20f5d3f61495f817204a5ddce89a7'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://xihulcjmmabslq:57e4eac48762e39558cc8872238cc817d2acbfceeab62737af25e03d6d9a7830@ec2-23-22-156-110.compute-1.amazonaws.com:5432/dedc0l9a6nh70r'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)


app.config.from_object(__name__)

from app import views
