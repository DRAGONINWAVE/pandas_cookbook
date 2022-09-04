import pandas as pd
import numpy  as np

crime = (pd.read_hdf(r'D:\python3.10\Pandas-Cookbook-master\data\crime.h5','crime')
              .set_index('REPORTED_DATE')
              .sort_index())

common_attrs = (set(dir(crime.index)) & set(dir(pd.Timestamp)))
print([attr for attr in common_attrs if attr[0] != '_'])

print(crime.index.day_name().value_counts())
print(crime
      .groupby(lambda idx:idx.day_name())
      [['IS_CRIME','IS_TRAFFIC']]
      .sum())
funcs = [lambda idx:idx.round('2h').hour,lambda idx:idx.year]
print(crime.groupby(funcs)
      [['IS_CRIME','IS_TRAFFIC']]
      .sum()
      .unstack()
)
print(crime.groupby(funcs)
      [['IS_CRIME','IS_TRAFFIC']]
      .sum()
      .unstack()
      .style.highlight_max(color='lightgrey')
)