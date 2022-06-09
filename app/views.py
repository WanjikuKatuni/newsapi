# where we will create our view functions
from flask import render_template #takes in the template file, searchers for it and loads it.
from app import app #app instance imported from app folder.

#views
@app.route('/')  #root dierctory created and defined as index.
def index():

    '''
    view root page function which returns the index page and its data
    '''

    message = 'Hello, here are some of the news we have got lined up for you'
    return render_template('index.html', message=message) #render templaete passes the index.html file created #first message is a vairable in the template, secodn message is the variabled in the view function/