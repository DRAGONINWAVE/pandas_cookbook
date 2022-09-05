import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

emp = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\employee.csv',
                  parse_dates=['HIRE_DATE','JOB_DATE'])
def yrs_exp(df_):
    days_hired = pd.to_datetime('12-1-2016') - df_.HIRE_DATE
    return days_hired.dt.days /365.25

emp = (emp.assign(YEARS_EXPERIENCE=yrs_exp))
print(emp[['HIRE_DATE','YEARS_EXPERIENCE']])

fig,ax = plt.subplots(figsize=(8,6))
sns.regplot(x='YEARS_EXPERIENCE',y='BASE_SALARY',
            data=emp,ax=ax)
fig.savefig('c13-scat4.png',dpi=300,bbox_inches='tight')

grid = sns.lmplot(x='YEARS_EXPERIENCE',y='BASE_SALARY',
                  hue='GENDER',palette='Greys',
                  scatter_kws={'s':10},data=emp)
grid.fig.set_size_inches(8,6)
grid.fig.savefig('c13-scat5.png',dpi=300,bbox_inches='tight')

grid = sns.lmplot(x='YEARS_EXPERIENCE',y='BASE_SALARY',
                  hue='GENDER',col='RACE',col_wrap=3,
                  palette='Greys',
                  line_kws={'linewidth':5},
                  data=emp)
grid.set(ylim=(20000,120000))
grid.fig.savefig('c13-scat6.png',dpi=300,bbox_inches='tight')

deps = emp['DEPARTMENT'].value_counts().index[:2]
races = emp['RACE'].value_counts().index[:3]
is_dep = emp['DEPARTMENT'].isin(deps)
is_race = emp['RACE'].isin(races)
emp2 = (emp[is_dep & is_race]
        .assign(DEPARTMENT=lambda df_:
                df_['DEPARTMENT'].str.extract('(HPD|HFD)',
                                              expand=True))
        )
print(emp2.shape)
print(emp2['RACE'].value_counts())

common_depts = (emp.groupby('DEPARTMENT')
                .filter(lambda group:len(group) > 50))
fig,ax = plt.subplots(figsize=(8,6))
sns.violinplot(x='YEARS_EXPERIENCE',y='GENDER',
               data=common_depts)
fig.savefig('c13-vio1.png',dpi=300,bbox_inches='tight')

grid = sns.catplot(x='YEARS_EXPERIENCE',y='GENDER',
                   col='RACE',row='DEPARTMENT',
                   height=3,aspect=2,
                   data=emp2,kind='violin')
grid.fig.savefig('c13-vio2.png',dpi=300,bbox_inches='tight')