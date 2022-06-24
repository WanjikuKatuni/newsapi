# where aplication will be initialised
#flask extensions need to be initialsied before they can be used for example bootstrap.
from flask import Flask 
from config import config_options
from flask_bootstrap import Bootstrap #import bootstrap class form the flaskbootstrap extension

bootstrap = Bootstrap()

def create_app(config_name): #create app funciton takes teh config setting key as an arguemnt
    
    app=Flask(__name__)

    app.config.from_object(config_options[config_name]) #from object imports configuration settings to the application

    bootstrap.init_app(app) #call init app as an extension to complete initialisation 

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app) #requests the request.py file

    return app 


# initializing application
#app = Flask(__name__, instance_relative_config = True)  #creating app instance #instance helps to connedt to instance folder created

#setup configuration
#app.config.from_object(DevConfig) #set up configuration and pass the devconfig subclass
#app.config.from_pyfile('config.py') #connects to the config.py file in inatnce folerd and its contents are appended to app.config

#init flask extension
#bootstrap = Bootstrap(app) #initialise thebootstrap class by passing in the app instance

#from app import views  #import views from app folder to create views
#from app import error #so that the error page can be initialised.