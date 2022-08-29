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

#college = (college
#           .groupby('STABBR')
#           ['UGDS']
#           .agg(max_deviation)
#           .round(1)
#           )
#print(college)

#college = (college
#           .groupby('STABBR')
#           [['UGDS','SATVRMID','SATMTMID']]
#           .agg(max_deviation)
#           .round(1))
#print(college)

#college = (college
#           .groupby(['STABBR','RELAFFIL'])
#           [['UGDS','SATVRMID','SATMTMID']]
#           .agg([max_deviation,'mean','std'])
#           .round(1)
#)
#print(college)

max_deviation.__name__ = 'Max Deviation'
college = (college
           .groupby(['STABBR','RELAFFIL'])
           [['UGDS','SATVRMID','SATMTMID']]
           .agg([max_deviation,'mean','std'])
           .round(1)
)
print(college)
