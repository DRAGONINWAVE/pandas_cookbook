import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt


employee = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\employee.csv',
                       parse_dates=['HIRE_DATE','JOB_DATE'])
print(employee)
fig,ax = plt.subplots(figsize=(8,6))
sns.countplot(y='DEPARTMENT',data=employee,ax=ax)
fig.savefig('c13-sns1.png',dpi=300,bbox_inches='tight')

fig,ax = plt.subplots(figsize=(8,6))
(employee['DEPARTMENT']
 .value_counts()
 .plot.barh(ax=ax))
fig.savefig('c13-sns2.png',dpi=300,bbox_inches='tight')

fig,ax = plt.subplots(figsize=(8,6))
sns.barplot(y='RACE',x='BASE_SALARY',data=employee,ax=ax)
fig.savefig('c13-sns3.png',dpi=300,bbox_inches='tight')

fig,ax = plt.subplots(figsize=(8,6))
(employee.groupby('RACE',sort=False)
 ['BASE_SALARY']
 .mean()
 .plot.barh(rot=0,width=.8,ax=ax)
 )
ax.set_xlabel('Mean Salary')
fig.savefig('c13-sns4.png',dpi=300,bbox_inches='tight')