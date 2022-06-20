class Article:
    '''
    article class to define article objects
    '''
    def __init__(self,id,source,title,author,description, image,link,date): #cdefine article class and create and init method that passes the six parameters inside the movie object.
        self.id=id
        self.source = source
        self.title=title
        self.description = description
        self.author=author
        self.image = image
        self.link = link
        self.date = date
      