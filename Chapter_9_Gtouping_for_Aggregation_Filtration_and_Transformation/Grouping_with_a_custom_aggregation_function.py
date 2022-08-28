import pandas as pd
import numpy  as np
college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv')
#college = (college
#           .groupby('STABBR')['UGDS']
#           .agg(['mean','std'])
#           .round(0)
#           )
#print(college)


def max_deviation(s):
    std_score = (s - s.mean()) / s.std()
    return std_score.abs().max()

college = (college
           .groupby('STABBR')
           ['UGDS']
           .agg(max_deviation)
           .round(1)
           )
print(college)