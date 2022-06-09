# where aplication will be initialised
from flask import Flask 
from .config import DevConfig

# initializing application
app = Flask(__name__)  #creating app instance

#setup configuration
app.config.from_object(DevConfig) #set up configuration and pass the devconfig subclass

from app import views  #import views from app folder to create views