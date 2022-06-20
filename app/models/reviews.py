# class Review:

#     all_reviews =[]

#     def __init__(self, article_source, title,imageurl,review):  #takes in the article id, review titie, image url and the review
#         self.article_source = article_source
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review

#     def save_review(self):
#         Review.all_reviews.append(self) #appends the review object to a calss variable alll_Reviews


#     @classmethod 
#     def clear_reviews(cls): #method that clears all items in the list
#         Review.all_reviews.clear()