from flask import Flask
from config import Config

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'you-will-never-guess' # or below
app.config.from_object('config.Config')

from app import views
