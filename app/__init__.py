# where aplication will be initialised
#flask extensions need to be initialsied before they can be used for example bootstrap.
from flask import Flask 
from .config import DevConfig
from flask_bootstrap import Bootstrap #import bootstrap class form the flaskbootstrap extension


# initializing application
app = Flask(__name__, instance_relative_config = True)  #creating app instance #instance helps to connedt to instance folder created

#setup configuration
app.config.from_object(DevConfig) #set up configuration and pass the devconfig subclass
app.config.from_pyfile('config.py') #connects to the config.py file in inatnce folerd and its contents are appended to app.config

#init flask extension
bootstrap = Bootstrap(app) #initialise thebootstrap class by passing in the app instance

from app import views  #import views from app folder to create views
from app import error #so that the error page can be initialised.