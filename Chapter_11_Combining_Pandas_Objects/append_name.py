from random import random
from turtle import pen
import pandas as pd
import numpy  as np
names = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\names.csv')
print(names.append({'Name':'Aria','Age':1},ignore_index=True))

names.index = ['Canada','Canada','USA','USA']
print(names)

s = pd.Series({'Name':'Zach','Age':3},name=len(names))
print(s)
print(names.append(s))

s1 = pd.Series({'Name':'Zach','Age':3},name=len(names))
s2 = pd.Series({'Name':'Zach','Age':2},name='USA')

print(names.append([s1,s1]))
bball_16 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\baseball16.csv')
print(bball_16)

data_dict = bball_16.iloc[0].to_dict()
print(data_dict)

new_data_dict = {k:'' if isinstance(v,str) else 
                 np.nan for k,v in data_dict.items()}
print(new_data_dict)

random_data = []
for i in range(1000):
    d = dict()
    for k,v in data_dict.items():
        if isinstance(v,str):
            d[k] = np.random.choice(list('abcde'))
        else:
            d[k] = np.random.randint(10)
    random_data.append(pd.Series(d,name=i+len(bball_16)))
print(random_data[0])
