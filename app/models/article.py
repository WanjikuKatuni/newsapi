class Article:
    '''
    article class to define article objects
    '''
    def __init__(self,id,title,overview, poster,vote_average,vote_count): #cdefine article class and create and init method that passes the six parameters inside the movie object.
        self.id=id
        self.title=title
        self.overview = overview
        self.poster = poster
        self.vote_average = vote_average
        self.vote_count = vote_count