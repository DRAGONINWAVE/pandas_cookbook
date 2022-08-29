import pandas as pd
import numpy  as np

movie = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\movie.csv')
actor = movie[['movie_title','actor_1_name',
               'actor_2_name','actor_3_name',
               'actor_1_facebook_li 2kes',
               'actor_2_facebook_likes',
               'actor_3_facebook_likes']]
print(actor.head())
def change_col_name(col_name):
    col_name = col_name.replace('_name','')
    if ''