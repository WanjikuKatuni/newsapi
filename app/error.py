# where handlers will be added for error pages

from flask import render_template
from app import app


@app.errorhandler(404) #passes in the error we receive
def four_ow_four(error): #vew fucntion tat returs the 4040
    '''
    function to render the 4040 error page
    '''
    return render_template('four_ow_four.html'),404