import pandas as pd
import numpy  as np

crime_sort = (pd.read_hdf(r'D:\python3.10\Pandas-Cookbook-master\data\crime.h5','crime')
              .set_index('REPORTED_DATE')
              .sort_index()
              )
print(crime_sort.resample('W'))
print(crime_sort
      .resample('W')
      .size()
      )
print(len(crime_sort.loc[:'2012-1-8']))
print(len(crime_sort.loc['2012-1-9':'2012-1-15']))
print(crime_sort
      .resample('W-THU')
      .size())
weekly_crimes = (crime_sort
                 .groupby(pd.Grouper(freq='W'))
                 .size())
print(weekly_crimes)
r = crime_sort.resample('W')
print([attr for attr in dir(r) if attr[0].islower()])

# resample crimes
crime = pd.read_hdf(r'D:\python3.10\Pandas-Cookbook-master\data\crime.h5','crime')
weekly_crimes2 = crime.resample('W',on='REPORTED_DATE').size()
print(weekly_crimes2.equals(weekly_crimes))
weekly_crimes_gb2 = (crime
                     .groupby(pd.Grouper(key='REPORTED_DATE',freq='W'))
                     .size()
)
print(weekly_crimes2.equals(weekly_crimes))
import matplotlib.pyplot as plt
fig,ax = plt.subplots(figsize=(16,4))
weekly_crimes.plot(title='ALL Denver Crimes',ax=ax)
fig.savefig('c12=crimes.png',dpi=300)