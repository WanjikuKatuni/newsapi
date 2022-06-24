# where we will create our view functions
from flask import redirect, render_template, request, url_for #takes in the template file, searchers for it and loads it.
from . import main
#from app import app #app instance imported from app folder.
from ..request import get_article, search_article #import the get articles function
# from .models import reviews
# from .forms import ReviewForm

# Review = reviews.Review


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
@main.route('/')  #root dierctory created and defined as index.
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
    
    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search', article_name = search_article))
    else:

        return render_template('index.html', title = title, article = top_articles) #render templaete passes the index.html file created #first message is a vairable in the template, secodn message is the variabled in the view function/

#add dynamic routes
# @app.route('/article/<int:article_id>') #part in angle brackets is dynamic and are redenred as strings whcih can be transformed into any type use int to transform it to an int.
# def article(article_id):

#     ''' 
#     view article page function which retruns article details and its data
#     '''
#     title = 'Here is the article requested'
#     return render_template('article.html',id = article_id, title=title)


#search option
@main.route('/everything/<article_name>')
def search(article_name):
    '''
    view function that displays search results
    '''

    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f"search results for {article_name}"
    return render_template('search.html', articles=searched_articles)



#review
# @app.route('/everything/review/new/<source>', methods = ['GET', 'POST']) #dynamic route for neww review function and pass the article ide, methods argument which registers the review funtion as  ahandler for get and post requests
# def new_review(source):
#     form = ReviewForm() #instance of reviews form class named as form
#     article = get_article(source) #to get the article object

#     if form.validate_on_submit(): #returns true when submitted form has been verified by the validators
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(article.source, title, article.image,review) #if validatoion is true, a new review object is created and saved
#         new_review.save_review()

#         return redirect(url_for('article',source=article.source)) #redirect the response to the article view function and pass in the article id

#     #if the validate on submit retunrs flase the new_Review.html from will be rendered and pass in the title, from object and article object.
#     title=f'{article.title} review'
#     return render_template ('new_review.html', title=title, review_form=form, article=article)