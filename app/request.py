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
base_url_article = app.config ["NEWS_API_ARTICLE_BASE_URL"]
base_url_source = app.config["NEWS_APISOURCE_BASE_URL"]


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
        source = article_item.get('source')
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

def get_article_id(id):
    get_article_details_url = base_url_article.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            id = article_details_response.get('id')
            source = article_details_response.get('source')
            title = article_details_response.get('title')
            author = article_details_response.get('author')
            description = article_details_response.get('description')
            link = article_details_response.get('url')
            img = article_details_response.get('urlToImage')
            date = article_details_response.get('publishedAt')
            
            print (img())
            article_object = Article(id,source,title,author,description,link,img, date)
    return article_object

#search for an article
def search_article(article_name):
    search_article_url ='https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'.format(article_name, api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results(search_article_list)

    return search_article_results
# get source of articles.

# def get_source(where):
#     get_article_source_url = base_url_source(where,api_key)

#     with urllib.request.urlopen(get_article_source_url) as url:
#         article_source_data = url.read()
#         article_source_response = json.loads(article_source_data)

#         article_sourceresults = None

#         if article_source_response['sources']:

#             article_source_resultslist = article_source_response['sources']
#             article_sourceresults = process_results(article_source_resultslist)

#     return article_sourceresults

# def process_results(article_sourcelist):
#     article_sourceresults= []
#     for articlesource_item in article_sourcelist:

#             id = articlesource_item.get('id')
#             name = articlesource_item.get('name')
#             link = articlesource_item.get('url')

#             articlesource_object = Article(id,name, link)
#             article_sourceresults.append(articlesource_object)

#     return article_sourceresults