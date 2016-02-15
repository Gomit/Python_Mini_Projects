# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:03:16 2015

@author: merongoitom
"""

import webbrowser

class Movie():
    """some text here"""
    valid_ratings = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
         
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)