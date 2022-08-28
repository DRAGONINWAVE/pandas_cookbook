from calendar import prcal
import pandas as pd
import numpy  as np

baseball_14 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\baseball14.csv',index_col='playerID')
baseball_15 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\baseball15.csv',index_col='playerID')
baseball_16 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\baseball16.csv',index_col='playerID')

print(baseball_14.head())
print(baseball_14.index.difference(baseball_15.index))
print(baseball_15.index.difference(baseball_14.index))
hits_14 = baseball_14['H']
hits_15 = baseball_15['H']
hits_16 = baseball_16['H']
print(hits_14.head())
print((hits_14 + hits_15).head())
print(hits_14.add(hits_15,fill_value=0).head())
hits_total = hits_14.add(hits_15,fill_value=0).add(hits_16,fill_value=0)
print(hits_total.head())
print(hits_total.hasnans)
s = pd.Series(index=['a','b','c','d'],data=[np.nan,3,np.nan,1])
print(s)
s1 = pd.Series(index=['a','b','c'],data=[np.nan,6,10])
print(s1)
print(s.add(s1,fill_value=5))
df_14 = baseball_14[['G','AB','R','H']]
df_15 = baseball_15[['H','AB','R','HR']]
print(df_14.head())
print(df_15.head())
print((df_14 + df_15).head(10).style.highlight_null('yellow'))