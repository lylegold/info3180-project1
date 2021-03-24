from flask import Flask
from .config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = "chubble"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:passwrod@localhost:5432/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
db = SQLAlchemy(app)


from app import views