import pandas as pd
import numpy  as np

employee = pd.read_csv(
    r'D:\python3.10\Pandas-Cookbook-master\data\employee.csv',index_col='RACE'
    )
print(
    employee.head())
salary1 = employee['BASE_SALARY']
salary1 = salary1.sort_index()
salary2 = employee['BASE_SALARY'].copy()
print(salary1.head())
print(salary2.head())

salary_add = salary1 + salary2
print(salary_add.head())
salary_add1 = salary1 + salary2
print(len(salary1),len(salary2),len(salary_add),len(salary_add1))
index_vc = salary1.index.value_counts(dropna=False)
print(index_vc)
print(index_vc.pow(2).sum())