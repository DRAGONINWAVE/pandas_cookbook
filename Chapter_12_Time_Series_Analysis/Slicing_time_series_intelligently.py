import pandas as pd
import numpy  as np

crime = pd.read_hdf(r'D:\python3.10\Pandas-Cookbook-master\data\crime.h5','crime')
print(crime.dtypes)
crime = crime.set_index('REPORTED_DATE')
print(crime)
print(crime.loc['2016-05-12 16:45:00'])
print(crime.loc['2016-05-12'])
print(crime.loc['2016-05'].shape)
print(crime.loc['2016'].shape)
print(crime.loc['2016-05-12 03'].shape)
print(crime.loc['Dec 2015'].sort_index())
print(crime.loc['2016 Sep,15'].shape)
print(crime.loc['21st October 2014 05'].shape)
print(crime.loc['2015-3-4':'2016-1-1'].sort_index())
print(crime.loc['2015-3-4 22':'2016-1-1 11:22:00'].sort_index())

mem_cat = crime.memory_usage().sum()
mem_obj = (crime
           .astype({'OFFENSE_TYPE_ID':'object',
                    'OFFENSE_CATEGORY_ID':'object',
                    'NEIGHBORHOOD_ID':'object'})
           .memory_usage(deep=True)
           .sum()
)
mb = 2**20
print((mem_cat / mb,1) ,round(mem_obj / mb ,1))
print(crime.index[:2])