# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:08:17 2015

@author: merongoitom
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.","http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc" )
avatar = media.Movie("Avatar","A marine on an alian planet","http://www.goldposter.com/wp-content/uploads/2015/05/Avatar_poster_goldposter_com_56.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY" )
spirited_away = media.Movie("Spirited Away","A little girl gets lost in a world far away","http://www.nausicaa.net/miyazaki/sen/poster_images/USA_full.jpg","https://www.youtube.com/watch?v=ByXuk9QqQkk" )

star_wars = media.Movie("Star Wars: The Force Awakens","Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a rag-tag group of heroes can stop them, along with the help of the Resistance.","http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster.jpg","https://www.youtube.com/watch?v=sGbxmsDFVnE" )
LOTR = media.Movie("Lord of the rings: The fellowship of the ring","A meek Hobbit and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron.","https://www.movieposter.com/posters/archive/main/105/MPW-52979","https://www.youtube.com/watch?v=Pki6jbSbXIY" )
SSR = media.Movie("The Shawshank Redemption","Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.","http://ecx.images-amazon.com/images/I/51SPVi-1rXL._SY355_.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco" )


#print (spirited_away.storyline)
#spirited_away.show_trailer()
movies = [toy_story,avatar, spirited_away, star_wars, LOTR, SSR]
#fresh_tomatoes.open_movies_page(movies)

#print media.Movie.valid_ratings
print media.Movie.__module__