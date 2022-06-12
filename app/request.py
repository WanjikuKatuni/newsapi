#write code that makes erquests to the api

from app import app #import flask appplicatio instance
import urllib.request,json #create connection to api url and send request to json to convert json repsonse to python dictionary
from .models import article

Article = article.Article

# getting api ket

api_key = app.config['NEWS_API_KEY']

# getting the article base url
#app.config is used to access configuration objects
base_url = app.config["NEWS_API_BASE_URL"]

def get_article(category): #get article function which will tkae in the article category as an argument

    '''
    function that gets the json repsonse to our url request
    '''
    get_article_url = base_url.format(category,api_key) #.format method to pass in category and api key in base url gw rmovies url becomes the final url in the api request

    with urllib.request.urlopen(get_article_url) as url: #with is a context manager that sends request using urllibrequest and takes in the get movies url as an argument and sends a request as url
        get_article_data = url.read() #read is used to read the url and store it in get article data variable
        get_article_response = json.loads(get_article_data) #convert json response to a python dictionary

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)

    return article_results