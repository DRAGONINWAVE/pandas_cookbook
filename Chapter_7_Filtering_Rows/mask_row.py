import pandas as pd 


movie = pd.read_csv(
    r'D:\python3.10\Pandas-Cookbook-master\data\movie.csv',index_col='movie_title')

c1 = movie['title_year'] >= 2010
c2 = movie['title_year'].isna()
criteria = c1 | c2
print(
    movie.mask(criteria).head()
)
movie_mask = movie.mask(criteria).dropna(how='all')
print(
    movie_mask.head()
    )

movie_boolean = movie[movie['title_year'] < 2010]
print(
    movie_mask.equals(movie_boolean)
    )
print(movie_mask.shape == movie_boolean.shape)
from pandas.testing import assert_frame_equal

assert_frame_equal(movie_boolean,movie_mask,check_dtype=False)