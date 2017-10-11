import fresh_tomatoes

import media

toy_story = media.Movie("Toy story",
	"A story of a boy and his toys that come to life",
	"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
					 "A historia de alienígenas",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
					 "https://www.youtube.com/watch?v=cWZ0cNTEbtk")

rocky6 = media.Movie("Rocky VI",
					 "A conclusão do clássico Rocky",
					 "http://www.filmesonlinegratis.com/wp-content/uploads/2015/05/Rocky-6.jpg",
					 "https://www.youtube.com/watch?v=qKNXWwRCLZs")

movies = [toy_story,avatar,rocky6]

fresh_tomatoes.open_movies_page(movies)
