from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://twvdtrzwqnioal:e2fXsAriasw3ZrvQwO9Sz5U4Q1@ec2-107-20-148-211.compute-1.amazonaws.com:5432/d3mncmq10ulio1'
app.config['SECRET_KEY'] = 'GGSB216737128edsgudsgdf #$$%^&89WEG{UDF}'
app.config['UPLOAD_FOLDER'] = "app/static"

db = SQLAlchemy(app)

from app import views, models
