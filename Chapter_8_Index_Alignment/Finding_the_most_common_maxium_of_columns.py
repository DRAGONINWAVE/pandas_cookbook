#from gc import collect
from locale import normalize
import pandas as pd
import numpy  as np


college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv',index_col='INSTNM')
college_ugds = college.filter(like='UGDS_')
print(college_ugds.head())
highest_percentage_race = college_ugds.idxmax(axis='columns')
print(highest_percentage_race.head())
print(highest_percentage_race.value_counts(normalize=True))
print(
    college_ugds[highest_percentage_race == 'UGDS_BLACK']
    .drop(columns='UGDS_BLACK')
    .idxmax(axis='columns')
    .value_counts(normalize))