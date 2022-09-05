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

fig,ax = plt.subplots(figsize=(18,6))
sns.barplot(x='RACE',y='BASE_SALARY',hue='GENDER',
            ax=ax,data=employee,palette='Greys',
            order=['Hispanic/Latino',
                   'Black or African American',
                   'American Indian or Alaskan Native',
                   'Asian/Pacific Islander',
                   'Others',
                   'White'])
fig.savefig('c13-sns.png',dpi=300,bbox_inches='tight')

fig,ax = plt.subplots(figsize=(18,6))
(employee.groupby(['RACE','GENDER'],sort=False)
 ['BASE_SALARY']
 .mean()
 .unstack('GENDER')
 .sort_values('Female')
 .plot.bar(rot=0,ax=ax,
           width=.8,cmap='viridis'))
fig.savefig('c13-sns.png',dpi=300,bbox_inches='tight')

fig,ax = plt.subplots(figsize=(8,6))
sns.boxplot(x='GENDER',y='BASE_SALARY',data=employee,
            hue='RACE',palette='Greys',ax=ax)
fig.savefig('c13-sns7.png',dpi=300,bbox_inches='tight')

fig,axs = plt.subplots(1,2,figsize=(12,6),sharey = True)
for g,ax in zip(['Female','Male'],axs):
    (employee
     .query('GENDER == @g')
     .assign(RACE=lambda df_:df_.RACE.fillna('NA'))
     .pivot(columns='RACE')
     ['BASE_SALARY']
     .plot.box(ax=ax,rot=30))
    ax.set_title(g+'Salary')
    ax.set_xlabel('')

fig.savefig('c13-sns8.png',bbox_inches='tight')