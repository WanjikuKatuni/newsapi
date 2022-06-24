
import unittest
from app.models import Article

#Article = article.Article #get the article class

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behavior of article class
    '''

    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_article = Article(1234, 'Newyork Times','whats new','Athrilling new python series', 'ann','poster','link','date')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

# if __name__ == '__main__':
#     unittest.main()