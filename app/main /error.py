# where handlers will be added for error pages

from flask import render_template
from . import main #import blueprint instance main and use it to define the ext decorator.


@main.app.errorhandler(404) #passes in the error we receive
def four_ow_four(error): #vew fucntion tat returs the 4040
    '''
    function to render the 4040 error page
    '''
    return render_template('four_ow_four.html'),404