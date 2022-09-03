import pandas as pd
import numpy  as np
import datetime

crime = pd.read_hdf(r'D:\python3.10\Pandas-Cookbook-master\data\crime.h5','crime').set_index('REPORTED_DATE')
print(crime.index)
print(crime.between_time('2:00','5:00',include_end=False))
print(crime.at_time('5:47'))
crime_sort = crime.sort_index()
print(crime_sort.first(pd.offsets.MonthBegin(6)))
print(crime_sort.first(pd.offsets.MonthEnd(6)))
print(crime_sort.first(pd.offsets.MonthEnd(6,normalize=True)))
print(crime_sort.loc[:'2012-06'])
print(crime_sort.first('5D'))
print(crime_sort.first('5B'))
print(crime_sort.first('7W'))
print(crime_sort.first('3QS'))
print(crime_sort.first('A'))
print(crime.between_time(datetime.time(2,0),datetime.time(5,0),
                         include_end=False))
first_date = crime_sort.index[0]
print(first_date)
print(first_date+pd.offsets.MonthBegin(6))
print(first_date+pd.offsets.MonthEnd(6))

step4 = crime_sort.first(pd.offsets.MonthEnd(6))
end_dt = crime_sort.index[0] + pd.offsets.MonthEnd(6)
step4_internal = crime_sort[:end_dt]
print(step4.equals(step4_internal))
dt = pd.Timestamp('2012-1-16 13:40')
print(dt + pd.DateOffset(months=1))
do  = pd.DateOffset(years=2,months=5,days=3,
                    hours=8,seconds=10)
print(pd.Timestamp('2012-1-22 03:22') + do)