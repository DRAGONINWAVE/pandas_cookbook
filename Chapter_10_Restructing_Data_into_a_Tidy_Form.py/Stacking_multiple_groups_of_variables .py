import pandas as pd
import numpy  as np

movie = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\movie.csv')
actor = movie[['movie_title','actor_1_name',
               'actor_2_name','actor_3_name',
               'actor_1_facebook_likes',
               'actor_2_facebook_likes',
               'actor_3_facebook_likes']]
print(actor.head())
def change_col_name(col_name):
    col_name = col_name.replace('_name','')
    if 'facebook' in col_name:
        fb_idx = col_name.find('facebook')
        col_name = (col_name[:5] + col_name[fb_idx - 1:]
                    + col_name[5:fb_idx-1])
    return col_name
actor2 = actor.rename(columns=change_col_name)
print(actor2)
stubs = ['actor','actor_facebook_likes']
actor2_tidy = pd.wide_to_long(actor2,
                              stubnames=stubs,
                              i=['movie_title'],
                              j='actor_num',
                              sep='_')
print(actor2_tidy.head())

df = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\stackme.csv')
print(df)
print(df.rename(columns = {'a1':'group1_a1','b2':'group1_b2',
                           'd':'group2_a1','e':'group2_b2'}))
print(pd.wide_to_long(
    df.rename(columns = {'a1':'group1_a1','b2':'group1_b2','d':'group2_a1','e':'group2_b2'}),
    stubnames=['group1','group2'],
    i=['State','Country','Test'],
    j='Lable',
    suffix='.+',
    sep='_')
)