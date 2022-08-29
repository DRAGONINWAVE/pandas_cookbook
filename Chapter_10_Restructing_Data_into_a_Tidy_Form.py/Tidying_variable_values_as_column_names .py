from calendar import prcal
from string import printable
import pandas as pd
import numpy  as np

state_fruit = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\state_fruit.csv',index_col=0)
print(state_fruit)
print(state_fruit.stack())
print(state_fruit.stack().reset_index())
print(state_fruit
      .stack()
      .reset_index()
      .rename(columns={'level_0':'state',
                       'level_1':'fruit',
                       0:'weight'})
)
print(state_fruit
      .stack()
      .rename_axis(['state','fruit']))
print(state_fruit
      .stack()
      .rename_axis(['state','fruit'])
      .reset_index(name='weight')
)

state_fruit2 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\state_fruit2.csv')
print(state_fruit2)
print(state_fruit2.stack())
print(state_fruit2.set_index('State').stack())