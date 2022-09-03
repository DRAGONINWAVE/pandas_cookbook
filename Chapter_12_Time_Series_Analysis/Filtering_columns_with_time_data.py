import pandas as pd
import numpy  as np

crime = pd.read_hdf(r'D:\python3.10\Pandas-Cookbook-master\data\crime.h5','crime')
print(crime.dtypes)
print(crime
      [crime.REPORTED_DATE == '2016-05-12 16:45:00'])

print(crime
      [crime.REPORTED_DATE == '2016-05-12'])
print(crime
      [crime.REPORTED_DATE.dt.date == '2016-05-12'])

print(crime
      [crime.REPORTED_DATE.between('2016-05-12','2016-5-13')])
print(crime
      [crime.REPORTED_DATE.between('2016-05','2016-6')].shape)
print(crime
      [crime.REPORTED_DATE.between('2016','2017')].shape)
print(crime
      [crime.REPORTED_DATE.between('2016-05-12 03','2016-5-12 04')].shape)
print(crime
      [crime.REPORTED_DATE.between('2016 Sep, 15','2016 Sep,16')].shape)
print(crime
      [crime.REPORTED_DATE.between('21st Sep 2014 05','21st Sep 2014 06')].shape)
print(crime
      [crime.REPORTED_DATE.between('2015-3-4','2016-1-1 23:59:59')].shape)

print(crime
      [crime.REPORTED_DATE.between('2015-3-4 22','2016-1-1 11:22:00')].shape)

