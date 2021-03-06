# configurations to meet the needs of the applications

import os  #allos app to interact with operating system dependent functionality

class Config: #contains configurations ued for both production and development stages
    '''
    general configuration parent class
    '''

    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?country=us&apiKey={}' #cur;y brackets represent sections of the url which will be replaced with actual values.
    NEWS_API_ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_APISOURCE_BASE_URL = 'https://newsapi.org/v1/{}?language=en&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY') #OS ENVIRON FUNCTION TO GET API KEY
    pass

class ProdConfig(Config): #subclass that contains configurations used in production stages and inherits from the parent config class.
    '''
    Production configuration child class

    Args:
         config: the parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config): #subclass which contains configurations used for development stages and inherits from the config class
    '''
    development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''

    DEBUG = True #enables debug mode in application

config_options = { #dictionaty config options to accfess configutation option calsses
    'development':DevConfig,
    'production': ProdConfig
}