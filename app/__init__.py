# where aplication will be initialised
from flask import Flask 

# initializing application
app = Flask(__name__)  #creating app instance

from app import views  #import views from app folder to create views