import pandas as pd
import numpy  as np

names = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\names.csv')
print(names)
new_data_list = ['Aria',1]
names.loc[4] = new_data_list
print(names)
names.loc['five'] = ['Zach',3]
print(names)
names.loc[len(names)] = {'Name':'Zayd','Age':2}
print(names)
names.loc[len(names)] = pd.Series({'Age':32,'Name':'Dean'})
print(names)
