import pandas as pd
import numpy  as np

college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv')

#def pct_between_1_3k(s):
#    return (
#        s.between(1_000,3_000)
#        .mean()
#        *100
#    )

#college = (college
#           .groupby(['STABBR','RELAFFIL'])
#           ['UGDS']
#           .agg(pct_between_1_3k)
#           .round(1)
#)
#print(college)

# 2nd function
#def pct_between(s,low,high):
#    return s.between(low,high).mean() * 100

#college = (college
#           .groupby(['STABBR','RELAFFIL'])
#           ['UGDS']
#           .agg(pct_between,1_000,10_000)
#           .round(1)
#)
#print(college)

# 3rd def def
def pct_between(s,low,high):
    return s.between(low,high).mean() * 100

def between_n_m(n,m):
    def wrapper(ser):
        return pct_between(ser,n,m)
    wrapper._name_ = f'between_{n}_{m}'
    return wrapper

college = (college
    .groupby(['STABBR','RELAFFIL'])
    ['UGDS']
    .agg([between_n_m(1_000,10_000),'max','mean'])
    .round(1)
    )
print(college)