from calendar import prcal
import pandas as pd
import numpy as np

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
movie_iloc = movie.iloc[criteria.to_numpy()]
print(
	movie_iloc.equals(movie_loc))

criteria_col  =movie.dtypes == np.int64
print(
	criteria_col.head())
print(movie.loc[:,criteria_col].head())
print(movie.iloc[:,criteria_col.to_numpy()].head())
cols = [
	'content_rating',
	'imdb_score',
	'title_year',
	'gross',
	]
print(movie.loc[criteria,cols].sort_values('imdb_score'))
col_index = [movie.columns.get_loc(col) for col in cols]
print(col_index)
a = criteria.to_numpy()
print(a[:5])
print(len(a),len(criteria))
print(movie.select_dtypes(int))