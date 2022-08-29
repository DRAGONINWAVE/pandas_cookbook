from itertools import groupby
import pandas as pd
import numpy  as np
from  IPython.display import display


college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv')
grouped  = college.groupby(['STABBR','RELAFFIL'])
print(grouped)
print([attr for attr in dir(grouped) if not attr.startswith('_')])
print(grouped.ngroups)
groups = list(grouped.groups)
print(groups[:6])
print(grouped.get_group(('FL',1)))

for name , group in grouped:
    print(name)
    display(group.head(3))

for name,group in grouped:
    print(name)
    print(group)
    break
print(grouped.head(2))
print(grouped.nth([1,-1]))