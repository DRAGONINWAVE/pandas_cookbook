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