import pandas as pd
import numpy  as np
flights = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\flights.csv')
print(flights.head())
print(flights.groupby('AIRLINE').agg({'ARR_DELAY':'mean'}))
print(flights.groupby('AIRLINE')['ARR_DELAY'].agg('mean'))
print(flights.groupby('AIRLINE')['ARR_DELAY'].agg(np.mean))
print(flights.groupby('AIRLINE')['ARR_DELAY'].mean())
grouped = flights.groupby('AIRLINE')
print(type(grouped))


# Grouping and aggregating with multiple columns and functions
print(flights.groupby(['AIRLINE','WEEKDAY'])['CANCELLED'].agg('sum'))
print(flights.groupby(['AIRLINE','WEEKDAY'])[['CANCELLED','DIVERTED']].agg(['sum','mean']))
print(flights.groupby(['ORG_AIR','DEST_AIR']).agg({'CANCELLED':['sum','mean','size'],'AIR_TIME':['mean','var']}))

print(flights.groupby(['ORG_AIR','DEST_AIR']).agg(sum_cancelled=pd.NamedAgg(column='CANCELLED',aggfunc='sum'),
                                                  mean_called=pd.NamedAgg(column='CANCELLED',aggfunc='mean'),
                                                  size_cancellded=pd.NamedAgg(column='CANCELLED',aggfunc='size'),
                                                  mean_air_time=pd.NamedAgg(column='AIR_TIME',aggfunc='mean'),
                                                  var_air_time=pd.NamedAgg(column='AIR_TIME',aggfunc='var')))

res = (flights
       .groupby(['ORG_AIR','DEST_AIR'])
       .agg({'CANCELLED':['sum','mean','size'],
             'AIR_TIME':['mean','var']}))
print(res)

