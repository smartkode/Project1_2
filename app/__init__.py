from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cvxtzukvylnave:sobDuj6be8BSex39QuKXQUEO9u@ec2-107-20-242-191.compute-1.amazonaws.com:5432/d657nrpn9952n2'
app.config['SECRET_KEY'] = 'GGSB216737128edsgudsgdf #$$%^&89WEG{UDF}'

# app.config['UPLOAD_FOLDER'] = '/home/rascal/Documents/WebDev2/flask/project1_2/app/static/img'
app.config['UPLOAD_FOLDER'] = '/app/static/img'

db = SQLAlchemy(app)
from app import views, models