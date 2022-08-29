import pandas as pd
import numpy  as np

flights = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\flights.csv')
flights_ct = flights.groupby(['ORG_AIR','DEST_AIR']).size()

print(flights_ct)
print(flights_ct.loc[[('ATL','IAH'),('IAH','ATL')]])

f_part3 = (flights[['ORG_AIR','DEST_AIR']]
           .apply(lambda ser : 
                  ser.sort_values().reset_index(drop=True),
                  axis='columns'))
print(f_part3)
rename_dict = {0:'AIR1',1:'AIR2'}
print(flights[['ORG_AIR','DEST_AIR']]
           .apply(lambda ser : 
                  ser.sort_values().reset_index(drop=True),
                  axis='columns')
           .rename(columns=rename_dict)
           .groupby(['AIR1','AIR2'])
           .size()
)
print(flights[['ORG_AIR','DEST_AIR']]
           .apply(lambda ser : 
                  ser.sort_values().reset_index(drop=True),
                  axis='columns')
           .rename(columns=rename_dict)
           .groupby(['AIR1','AIR2'])
           .size()
           .loc[('ATL','IAH')]
)

data_sorted = np.sort(flights[['ORG_AIR','DEST_AIR']])
print(data_sorted[:10])