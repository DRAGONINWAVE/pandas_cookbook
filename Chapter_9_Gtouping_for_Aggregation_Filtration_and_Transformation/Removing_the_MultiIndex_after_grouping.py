import pandas as pd 
import numpy  as np

flights = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\flights.csv')
airline_info = (flights
                .groupby(['AIRLINE','WEEKDAY'])
                .agg({'DIST':['sum','mean'],
                      'ARR_DELAY':['min','max']})
                .astype(int)
                )
print(airline_info)
print(airline_info.columns.get_level_values(0))
print(airline_info.columns.to_flat_index())
airline_info.columns = ['_'.join(x) for x in 
                        airline_info.columns.to_flat_index()]
print(airline_info)
print(airline_info.reset_index())
#flights = (flights
# .groupby(['AIRLINE','WEEKDAY'])
# .agg(dist_sum=pd.NamedAgg(column='DIST',aggfunc='sum'),
#      dist_mean=pd.NamedAgg(column='DIST',aggfunc='mean'),
#      arr_delay_min=pd.NamedAgg(column='ARR_DELAY',aggfunc='min'),
#      arr_delay_max=pd.NamedAgg(column='ARR_DELAY',aggfunc='max'))
# .astype(int)
# .reset_index())
#print(flights)
flights = (flights
           .groupby(['AIRLINE'],as_index=False)
           ['DIST']
           .agg('mean')
           .round(0)
           )
print(flights)