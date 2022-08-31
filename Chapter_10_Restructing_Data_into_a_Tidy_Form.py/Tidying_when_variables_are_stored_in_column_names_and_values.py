import pandas as pd

sensors = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\sensors.csv')
print(sensors)
print(sensors.melt(id_vars=['Group','Property'],var_name='Year'))
print(sensors
      .melt(id_vars=['Group','Property'],var_name='Year')
      .pivot_table(index=['Group','Year'],
                   columns='Property',values='value')
      .reset_index()
      .rename_axis(None,axis='columns')
)

print(
    sensors
    .set_index(['Group','Property'])
    .rename_axis('Year',axis='columns')
    .stack()
    .unstack('Property')
    .rename_axis(None,axis='columns')
    .reset_index()
    )