from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import sha3_512
from os import urandom


app = Flask(__name__)
app.config['SECRET_KEY'] = sha3_512(urandom(24)).hexdigest()
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://info3180:project1@localhost/info3180_project1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)


app.config.from_object(__name__)

from app import views
