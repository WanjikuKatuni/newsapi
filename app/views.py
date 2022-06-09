# where we will create our view functions
from flask import render_template #takes in the template file, searchers for it and loads it.
from app import app #app instance imported from app folder.

#views
@app.route('/')  #root dierctory created and defined as index.
def index():

    '''
    view root page function which returns the index page and its data
    '''

    return render_template('index.html') #render templaete passes the index.html file created