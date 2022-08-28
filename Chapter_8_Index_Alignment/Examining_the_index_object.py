import pandas as pd 
import numpy as np


college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv')
columns = college.columns
print(
    columns)
print(columns.values)
print(
    columns.min(),columns.max(),columns.isnull().sum()
    )
columns = columns + '_A'
print(columns)
c1 = columns[:4]
c2 = columns[2:6]
c1 = c1.union(c2) # or 'c1 | c2'
print(
    c1)
c1 = c1.symmetric_difference(c2) # or ' c1^ c2'
print(c1)