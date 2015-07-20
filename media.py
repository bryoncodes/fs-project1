#!/usr/bin/python

# import the provided module
import fresh_tomatoes

# define movie class
# constructor takes the following parameters:
#   string with movie title
#   string with url to poster art
#   string with url to trailer on YouTube
#   list of strings of actors
class movie:

    def __init__ (self,title, art_url, trailer_url, actors):
        self.trailer_youtube_url = trailer_url
        self.poster_image_url = art_url
        self.title = title
        self.actors = actors

#instantiate some movie objects
m1 = movie("Idiocracy", "http://i.imgur.com/UWHnbYv.jpg", "https://www.youtube.com/watch?v=BBvIweCIgwk", ["Luke Wilson", "Maya Rudolph", "Justin Long"])
m2 = movie("Full Metal Jacket", "http://i.imgur.com/k67OMUe.jpg", "https://www.youtube.com/watch?v=x9f6JaaX7Wg", ["R. Lee Ermy", "Matthew Modine", "Adam Baldwin"] )
m3 = movie("Office Space", "http://i.imgur.com/952MNeQ.jpg", "https://www.youtube.com/watch?v=_IwzZYRejZQ", ["Ron Livingstone", "Jennifer Aniston", "Gary Cole"] )
m4 = movie("Sling Blade", "http://i.imgur.com/K5OESky.jpg", "https://www.youtube.com/watch?v=4sQuu36ZKQg", ["Billy Bob Thornton", "Dwight Yoakum", "John Ritter"] )
m5 = movie("Blazing Saddles", "http://i.imgur.com/JP0vley.jpg", "https://www.youtube.com/watch?v=iLNQv19YpG4", ["Cleavon Little", "Gene Wilder", "Madeline Kahn"] )

# put instantiated objects in a list
movies = [m1, m2, m3, m4, m5]

# call function to generate html
fresh_tomatoes.open_movies_page(movies)
