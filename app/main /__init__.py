#this subfolder defines the bluprint
#bluepritn is an application whcih deifnes routes

from flask import Blueprint
main = Blueprint('main', __name__) #initialise bluepritn class and it takes two arguemnts, the name of the b;ue print and the name variable to find location of blueprint.
from . import views,error #to avoid circular dependencies we improt the views and errors modules.