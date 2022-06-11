# where aplication will be initialised
from flask import Flask 
from .config import DevConfig

# initializing application
app = Flask(__name__, instance_relative_config = True)  #creating app instance #instance helps to connedt to instance folder created

#setup configuration
app.config.from_object(DevConfig) #set up configuration and pass the devconfig subclass
app.config.from_pyfile('config.py') #connects to the config.py file in inatnce folerd and its contents are appended to app.config

from app import views  #import views from app folder to create views