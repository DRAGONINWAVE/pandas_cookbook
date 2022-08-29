import pandas as pd
import numpy  as np

s = pd.Series([0,1,1,0,1,1,1,0])
print(s)
s1 = s.cumsum()
print(s1)
print(s.mul(s1))
print(s.mul(s1).diff())
print(s.mul(s.cumsum())
      .diff()
      .where(lambda x : x < 0)
)
print(s.mul(s.cumsum())
      .diff()
      .where(lambda x : x < 0)
      .ffill()
)
print(s.mul(s.cumsum())
      .diff()
      .where(lambda x : x < 0)
      .ffill()
      .add(s.cumsum(),fill_value=0)
)
flights = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\flights.csv')
print(flights
      .assign(ON_TIME=flights['ARR_DELAY'].lt(15).astype(int))
      [['AIRLINE','ORG_AIR','ON_TIME']]
)

def max_streak(s):
    s1 = s.cumsum()
    return(
        s.mul(s1)
        .diff()
        .where(lambda x : x < 0)
        .ffill()
        .add(s1,fill_value=0)
        .max()
    )
print(
    flights
    .assign(ON_TIME=flights['ARR_DELAY'].lt(15).astype(int))
    .sort_values(['MONTH','DAY','SCHED_DEP'])
    .groupby(['AIRLINE','ORG_AIR'])
    ['ON_TIME']
    .agg(['mean','size',max_streak])
    .round(2)
)

def max_delay_streak(df):
    df = df.reset_index(drop=True)
    late = 1 - df['ON_TIME']
    late_sum = late.cumsum()
    streak = (late
              .mul(late_sum)
              .diff()
              .where(lambda x: x< 0)
              .ffill()
              .add(late_sum,fill_value=0)
    )
    last_idx = streak.idxmax()
    first_idx = last_idx - streak.max() + 1
    res = (df
           .loc[[first_idx,last_idx],['MONTH','DAY']]
           .assign(streak = streak.max())
    )
    res.index = ['first','last']
    return res


print(flights
      .assign(ON_TIME=flights['ARR_DELAY'].lt(15).astype(int))
      .sort_values(['MONTH','DAY','SCHED_DEP'])
      .groupby(['AIRLINE','ORG_AIR'])
      .apply(max_delay_streak)
      .sort_values('streak',ascending=False)
      )