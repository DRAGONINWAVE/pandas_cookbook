import pandas as pd
import numpy  as np

flights= pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\flights.csv')
fpt = flights.pivot_table(index='AIRLINE',
                          columns='ORG_AIR',
                          values='CANCELLED',
                          aggfunc='sum',
                          fill_value=0)
print(fpt)
print(flights
      .groupby(['AIRLINE','ORG_AIR'])
      ['CANCELLED']
      .sum()
)
fpg = (flights
      .groupby(['AIRLINE','ORG_AIR'])
      ['CANCELLED']
      .sum()
      .unstack('ORG_AIR',fill_value=0)
)
print(fpt.equals(fpg))

print(flights.pivot_table(index=['AIRLINE','MONTH'],
                          columns=['ORG_AIR','CANCELLED'],
                          values=['DEP_DELAY','DIST'],
                          aggfunc=['sum','mean'],
                          fill_value=0)
)
print(flights
      .groupby(['AIRLINE','MONTH','ORG_AIR','CANCELLED'])
      [['DEP_DELAY','DIST']]
      .agg(['mean','sum'])
      .unstack(['ORG_AIR','CANCELLED'],fill_value=0)
      .swaplevel(0,1,axis='columns')
)