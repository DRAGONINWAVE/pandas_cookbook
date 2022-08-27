import pandas as pd

movie = pd.read_csv(
	r'D:\python3.10\Pandas-Cookbook-master\data\movie.csv',
	index_col='movie_title'
	)
c1 = movie['content_rating'] == 'G'
c2 = movie['imdb_score'] < 4
criteria = c1 & c2
movie_loc = movie.loc[criteria]
print(movie_loc.head())
print(movie_loc.equals(movie[criteria]))