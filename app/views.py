# where we will create our view functions
from flask import render_template #takes in the template file, searchers for it and loads it.
from app import app #app instance imported from app folder.

#views
@app.route('/')  #root dierctory created and defined as index.
def index():

    '''
    view root page function which returns the index page and its data
    '''

    title = 'Welcome, Here are some of the news we have got lined up for you'
    return render_template('index.html', title = title) #render templaete passes the index.html file created #first message is a vairable in the template, secodn message is the variabled in the view function/

#add dynamic routes
@app.route('/article/<int:article_id>') #part in angle brackets is dynamic and are redenred as strings whcih can be transformed into any type use int to transform it to an int.
def article(article_id):

    ''' 
    view article page function which retruns article details and its data
    '''
    title = 'Here is the article requested'
    return render_template('article.html',id = article_id, title=title)
