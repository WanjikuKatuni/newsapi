# where we will create our view functions
from flask import render_template #takes in the template file, searchers for it and loads it.
from app import app #app instance imported from app folder.
from .request import get_article  #import the get articles function
#from newsapi import NewsApiClient

#initialising newsapi
#newsapi= NewsApiClient(api_key='206c52b0288342de8f6d76f653647450')



#sources
# @app.route('/')
# def index():
#     ''' 
#     root page which returns most notable sources available
#     '''
#     top_sources = get_article('top-headlines/sources')
#     print(top_sources)
#     return render_template ('index.html', article_source = top_sources)
# #top articles
@app.route('/')  #root dierctory created and defined as index.
def index():

    '''
    view root page function which returns the index page and its data
    '''


    #getting topheadlines
    #top_headlines = get_article('articles') #to get the popular article from the api
    #print(news_articles)

    # get top_headlines
    #top_headlines = newsapi.get_top_headlines(sources='bbc-news, abc-news, cnn, nfl-news', language='en')
    #print(top_headlines)
    # news sources
    #news_sources = get_source('sources')
    #print(news_sources)
    #geting toparticles
    top_articles = get_article('top-headlines')
    #all_articles = get_article('everything')
    #print(top_articles)
    title = 'Welcome, Here are some of the news we have got lined up for you'
    return render_template('index.html', title = title, article = top_articles) #render templaete passes the index.html file created #first message is a vairable in the template, secodn message is the variabled in the view function/

#add dynamic routes
# @app.route('/article/<int:article_id>') #part in angle brackets is dynamic and are redenred as strings whcih can be transformed into any type use int to transform it to an int.
# def article(article_id):

#     ''' 
#     view article page function which retruns article details and its data
#     '''
#     title = 'Here is the article requested'
#     return render_template('article.html',id = article_id, title=title)
