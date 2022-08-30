from statistics import mean
import pandas as pd
import numpy  as np

def usecol_func(name):
    return 'UGDS_' in name or name == 'INSTNM'

college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv',
                      index_col='INSTNM',
                      usecols=usecol_func)
print(college)
college_stacked = college.stack()
print(college_stacked)
print(college_stacked.unstack())
college2 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv',
                       usecols=usecol_func)
print(college2)
college_melted = college2.melt(id_vars='INSTNM',
                               var_name='Race',
                               value_name='Percentage')
print(college_melted)
melted_inv = college_melted.pivot(index='INSTNM',
                                  columns='Race',
                                  values='Percentage')
print(melted_inv)

college2_replication = (melted_inv.loc[college2['INSTNM'],college2.columns[1:]]
                        .reset_index())
print(college2.equals(college2_replication))
print(college.stack().unstack(0))
print(college.T)
employee = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\employee.csv')
print(employee
      .groupby('RACE')
      ['BASE_SALARY']
      .mean()
      .astype(int)
      )
print(employee
      .groupby(['RACE','GENDER'])
      ['BASE_SALARY']
      .mean()
      .astype(int)
      )
print(employee
      .groupby(['RACE','GENDER'])
      ['BASE_SALARY']
      .mean()
      .astype(int)
      .unstack('GENDER')
      )
print(employee
      .groupby(['RACE','GENDER'])
      ['BASE_SALARY']
      .mean()
      .astype(int)
      .unstack('RACE')
      )
print(employee
      .groupby(['RACE','GENDER'])
      ['BASE_SALARY']
      .agg(['mean','max','min'])
      .astype(int)
      #.unstack('RACE')
      )
print(employee
      .groupby(['RACE','GENDER'])
      ['BASE_SALARY']
      .agg(['mean','max','min'])
      .astype(int)
      .unstack('GENDER')
      )