import pandas as pd
import numpy  as np
import datetime

date = datetime.date(year=2013,month=6,day=7)
time = datetime.time(hour=12,minute=30,
                     second=19,microsecond=463198)
dt = datetime.datetime(year=2013,month=6,day=7,
    hour=12,minute=30,
    second=19,microsecond=463198)

print(f'date is {date}')
print(f'time is {time}')
print(f'datetime is {dt}')

td  =datetime.timedelta(weeks=2,days=5,hours=10,
                        minutes=20,seconds=6.73,
                        milliseconds=99,microseconds=8)
print(td)
print(f'new date is {date+td}')
print(f'new datetime is {dt+td}')

print(pd.Timestamp(year=2012,month=12,day=21,hour=5,
                   minute=10,second=8,microsecond=99))
print(pd.Timestamp('2016/1/10'))
print(pd.Timestamp('2016-5/10'))
print(pd.Timestamp('Jan 3,2019 20:45.56'))
print(pd.Timestamp('2016-01-05T05:34:43.123456789'))
print(pd.Timestamp(500))
print(pd.Timestamp(5000,unit='D'))
print(pd.to_datetime('2015-5-13'))
print(pd.to_datetime('2015-13-5',dayfirst=True))
#print(pd.to_datetime('Start Date: Sep 30, 2017 Start Time: 1:30 pm',
#                     format='Start Date: %b %d,%Y Start Time: %I:%M %p'))
print(pd.to_datetime(100,unit='D',origin='2013-1-1'))
s = pd.Series([10,100,1000,10000])
print(pd.to_datetime(s,unit='D'))
s = pd.Series(['12-5-2015','14-1-2013','20/12/2017','40/23/2017'])
print(pd.to_datetime(s,dayfirst=True,errors='coerce'))
print(pd.to_datetime(['Aug 3 1999 3:45:56','10/31/2017']))
print(pd.Timedelta('12 days 5 hours 3 minutes 123456789 nanoseconds'))
print(pd.Timedelta(days=5,minutes=7.34))
print(pd.Timedelta(100,unit='W'))
print(pd.to_timedelta('67:15:45.454'))
s = pd.Series([10,100])
print(pd.to_timedelta(s,unit='s'))
time_strings=['2 days 24 minutes 89.67 seconds','00:45:23.6']
print(pd.to_timedelta(time_strings))
print(pd.Timedelta('12 days 5 hours 3 minutes') * 2)
td1 = pd.to_timedelta([10,100],unit='s')
td2 = pd.to_timedelta(['3 hours','4 hours'])
print(td1 + td2)
print(pd.Timedelta('12 days')/pd.Timedelta('3 days'))
ts = pd.Timestamp('2016-10-1 4:23:23.9')
print(ts.ceil('h'))
print(ts.year,ts.month,ts.day,ts.hour,ts.minute,ts.second)
print(ts.dayofweek,ts.dayofyear,ts.daysinmonth)

print(ts.to_pydatetime())
td = pd.Timedelta(125.8723,unit='h')
print(td)
print(td.round('min'))
print(td.components)
print(td.total_seconds())