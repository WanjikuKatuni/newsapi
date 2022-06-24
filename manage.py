from app import create_app
from flask_script import Manager,Server

#CREATING APP INSTANCE
app = create_app('development') #call the create app function and pass in the config options key soa s to create app instance

#initilaise the manage class by passing app instance
manager = Manager(app)

manager.add_command('server', Server) #add command creates a new command whcih will launch server to our aplication.

if __name__ == '__main__': #runs the application
    manager.run()