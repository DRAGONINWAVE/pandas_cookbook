from tokenize import group
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

crime = (pd.read_hdf(r'D:\python3.10\Pandas-Cookbook-master\data\crime.h5','crime')
              .set_index('REPORTED_DATE')
              .sort_index()
              )
print(crime
      .resample('Q')
      [['IS_CRIME','IS_TRAFFIC']]
      .sum()
      )
print(crime
      .resample('QS')
      [['IS_CRIME','IS_TRAFFIC']]
      .sum()
      )
print(crime
      .loc['2012-4-1':'2012-6-30',['IS_CRIME','IS_TRAFFIC']]
      .sum()
)
print(crime
      .groupby(pd.Grouper(freq='Q'))
      [['IS_CRIME','IS_TRAFFIC']]
      .sum()
)
fig,ax = plt.subplots(figsize=(16,4))

p = (crime
     .groupby(pd.Grouper(freq='Q'))
     [['IS_CRIME','IS_TRAFFIC']]
     .sum()
     .plot(color=['black','lightgrey'],ax=ax,
           title='Denver Crimes and traffic Acciernts')
)
fig.savefig('c12-crimes2.png',dpi=300)
print(crime
      .resample('Q')
      .sum())
print(crime
      .resample('QS-MAR')
      [['IS_CRIME','IS_TRAFFIC']]
      .sum()
      )
crime_begin = (crime.resample('Q')
               [['IS_CRIME','IS_TRAFFIC']]
               .sum()
               .iloc[0]
               )
fig, ax = plt.subplots(figsize=(16,4))
p = (crime
     .resample('Q')
     [['IS_CRIME','IS_TRAFFIC']]
     .sum()
     .div(crime_begin)
     .sub(1)
     .round(2)
     .mul(100)
     .plot.bar(color=['black','lightgrey'],ax=ax,
               title = 'Denver Crimes and Traffic Accidents % Increase')
     )
fig.autofmt_xdate()
fig.savefig('c12-crimes3.png',dpi=300,bbox_inches='tight')
