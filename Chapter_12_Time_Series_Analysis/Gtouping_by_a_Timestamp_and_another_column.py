import pandas as pd
import numpy  as np

employee = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\employee.csv',
                       parse_dates=['JOB_DATE','HIRE_DATE'],
                       index_col='HIRE_DATE')
print(employee)
print(employee
      .groupby('GENDER')
      ['BASE_SALARY']
      .mean()
      .round(-2))
print(employee
      .resample('10AS')
      ['BASE_SALARY']
      .mean()
      .round(-2))
print(employee
      .groupby('GENDER')
      .resample('10AS')
      ['BASE_SALARY']
      .mean()
      .round(-2))
print(employee
      .groupby('GENDER')
      .resample('10AS')
      ['BASE_SALARY']
      .mean()
      .round(-2)
      .unstack('GENDER')
      )
print(employee[employee['GENDER'] == 'Male'].index.min())
print(employee[employee['GENDER'] == 'Female'].index.min())
print(employee
      .groupby(['GENDER',pd.Grouper(freq='10AS')])
      ['BASE_SALARY']
      .mean()
      .round(-2)
      .unstack('GENDER')
      )

sal_final = (employee
      .groupby(['GENDER',pd.Grouper(freq='10AS')])
      ['BASE_SALARY']
      .mean()
      .round(-2)
      .unstack('GENDER')
      )
years = sal_final.index.year
years_right = years +9
sal_final.index = years.astype(str) + '-' + years_right.astype(str)
print(sal_final)

cuts = pd.cut(employee.index.year,bins=5,precision=0)
print(cuts.categories.values)
print(employee
      .groupby([cuts,'GENDER'])
      ['BASE_SALARY']
      .mean()
      .unstack('GENDER')
      .round(-2))