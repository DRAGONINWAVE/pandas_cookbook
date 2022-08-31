import pandas as pd

inspections = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\restaurant_inspections.csv',
                          parse_dates=['Date'])
print(inspections)
print(inspections.set_index(['Name','Date','Info']))
print(inspections.set_index(['Name','Date','Info'])
      .unstack('Info'))
print(
    inspections
    .set_index(['Name','Date','Info'])
    .unstack('Info')
    .reset_index(col_level=-1))
print(
    inspections
    .set_index(['Name','Date','Info'])
    .unstack('Info')
    .reset_index(col_level=-1)
    .droplevel(0,axis=1)
    .rename_axis(None,axis=1))
print(
    inspections
    .set_index(['Name','Date','Info'])
    .squeeze()
    .unstack('Info')
    .reset_index()
    #.droplevel(0,axis=1)
    .rename_axis(None,axis='columns'))
print((inspections
      .pivot_table(index=['Name','Date'],
      columns='Info',
      values='Value',
      aggfunc='first'))
      .reset_index()
      .rename_axis(None,axis='columns')
)