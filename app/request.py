#write code that makes erquests to the api

from app import app #import flask appplicatio instance
import urllib.request,json #create connection to api url and send request to json to convert json repsonse to python dictionary
from .models import article
#from newsapi import NewsApiClient

Article = article.Article

# getting api ket
api_key = app.config['NEWS_API_KEY']

#initialise news api
#newsapi = NewsApiClient(api_key)

# getting the article base url
#app.config is used to access configuration objects
base_url = app.config["NEWS_API_BASE_URL"]

def get_article(category): #get article function which will tkae in the article category as an argument
    
    '''
    function that gets the json repsonse to our url request
    '''
    
    #top_headlines = newsapi.get_top_headlines()['totalResults']
    get_article_url = base_url.format(category,api_key) #.format method to pass in category and api key in base url gw rmovies url becomes the final url in the api request

    with urllib.request.urlopen(get_article_url) as url: #with is a context manager that sends request using urllibrequest and takes in the get movies url as an argument and sends a request as url
        get_article_data = url.read() #read is used to read the url and store it in get article data variable
        get_article_response = json.loads(get_article_data) #convert json response to a python dictionary

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)

    return article_results

#function that will process the resutls and create article objects from the elements we need.

def process_results(article_list): #the function process results takes in a list of dictionaries 
    '''
    funciton that porcess the article result and transform them to a list of objects
    
    Args:
    article_list: a list of dictionaries that contain the article detials
    
    
    Returns:
    article_results: A list of movie objects
    '''
    article_results = [] #empty so that it can store the newly created article objects
    for article_item in article_list: #loop the list of dictionaties using the get method to pass in the keys so we can access the values
        id = article_item.get('id')
        source = article_item.get('name')
        title = article_item.get('title')
        author = article_item.get('author')
        description = article_item.get('description')
        link = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if image: #check if some articles have images, if not they are not displayed
            article_object = Article(id,source,title,author,description,link,image,date) #values gotten are added to the new article object
            article_results.append(article_object) #new article object is appeded to the empty article results list

    return article_results #return the list with the article objects
