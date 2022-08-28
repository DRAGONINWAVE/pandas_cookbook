import pandas as pd
import numpy  as np

employee = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\employee.csv')
dept_sal = employee[['DEPARTMENT','BASE_SALARY']]
dept_sal = dept_sal.sort_values(['DEPARTMENT','BASE_SALARY'],ascending=[True,False])


max_dept_sal = dept_sal.drop_duplicates(subset='DEPARTMENT')
print(max_dept_sal.head())
max_dept_sal = max_dept_sal.set_index('DEPARTMENT')
employee = employee.set_index('DEPARTMENT')

employee = employee.assign(
    MAX_DEPT_SALARY=max_dept_sal['BASE_SALARY'])
print(employee)

random_salary = dept_sal.sample(n=10,random_state=42).set_index('DEPARTMENT')
print(random_salary)
max_sal = (
    employee
    .groupby('DEPARTMENT')
    .BASE_SALARY
    .transform('max'))
print(employee.assign(MAX_DEPT_SALARY=max_sal))
sax_sal = (
    employee.groupby('DEPARTMENT')
    .BASE_SALARY.max())
employee.merge(
    max_sal.rename('MAX_DEPT_SALARY'),
    how='left',
    left_on='DEPARTMENT',
    right_index=True)
print(employee)