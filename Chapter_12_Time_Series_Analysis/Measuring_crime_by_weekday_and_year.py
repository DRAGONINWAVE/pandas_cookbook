import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt


crime = pd.read_hdf(r'D:\python3.10\Pandas-Cookbook-master\data\crime.h5','crime')
print(crime)
print(crime['REPORTED_DATE']
      .dt.day_name()
      .value_counts())
days = ['Monday','Tuesday','Wednesday','Thursday',
        'Friday','Saturday','Sunday']
title = 'Denver Crimes and Traffic Accidents per Weekday'
fig,ax=plt.subplots(figsize=(6,4))
p = (crime['REPORTED_DATE']
     .dt.day_name()
     .value_counts()
     .reindex(days)
     .plot.barh(title=title,ax=ax)
)
fig.savefig('c12-crimes4.png',dpi=300,bbox_inches='tight')

title = 'Denver Crimes and Traffi Accidents per Year'
fig,ax =plt.subplots(figsize=(6,4))
p = crime['REPORTED_DATE'].dt.year.value_counts().sort_index().plot.barh(title=title,ax=ax)
fig.savefig('c12-crimes.png',dpi=300,bbox_inches='tight')

print(crime
      .groupby([crime['REPORTED_DATE'].dt.year.rename('year'),
                crime['REPORTED_DATE'].dt.day_name().
                rename('day')])
      .size())

print(crime
      .groupby([crime['REPORTED_DATE'].dt.year.rename('year'),
                crime['REPORTED_DATE'].dt.day_name().
                rename('day')])
      .size()
      .unstack('day')
      )
criteria = crime['REPORTED_DATE'].dt.year == 2017
print(crime.loc[criteria,'REPORTED_DATE'].dt.dayofyear.max())
print(round(272/365,3))

crime_pct = (crime['REPORTED_DATE']
             .dt.dayofyear.le(272)
             .groupby(crime.REPORTED_DATE.dt.year)
             .mean()
             .mul(100)
             .round(2))
print(crime_pct)
print(crime_pct.loc[2012:2016].median())

def update_2017(df_):
    df_.loc[2017] = (df_
                     .loc[2017]
                     .div(.748)
                     .astype('int')
                     )
    return df_

print(
    crime
    .groupby([crime['REPORTED_DATE'].dt.year.rename('year'),
              crime['REPORTED_DATE'].dt.day_name().
              rename('day')])
    .size()
    .unstack('day')
    .pipe(update_2017)
    .reindex(columns=days)
    )

import seaborn as sns
fig,ax = plt.subplots(figsize=(6,4))
table = (crime
         .groupby([crime['REPORTED_DATE'].dt.year.rename('year'),
                   crime['REPORTED_DATE'].dt.day_name().rename('day')])
         .size()
         .unstack('day')
         .pipe(update_2017)
         .reindex(columns=days)
         )
sns.heatmap(table,cmap='Greys',ax=ax)
fig.savefig('c12-crimes6.png',dpi=300,bbox_inches='tight')

denver_pop = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\denver_pop.csv',
                         index_col='Year')
print(denver_pop)

den_100k = denver_pop.div(100_000).squeeze()
normalized = (crime
              .groupby([crime['REPORTED_DATE'].dt.year.rename('year'),
                        crime['REPORTED_DATE'].dt.day_name().rename('day')])
              .size()
              .unstack('day')
              .pipe(update_2017)
              .reindex(columns=days)
              .div(den_100k,axis='index')
              .astype(int)
              )
print(normalized)

import seaborn as sns
fig,ax = plt.subplots(figsize=(6,4))
sns.heatmap(normalized,cmap='Greys',ax=ax)
fig.savefig('c12-crimes7.png',dpi=300,bbox_inches='tight')

print(crime
      ['REPORTED_DATE']
      .dt.day_name()
      .value_counts()
      .loc[days])

print(crime
      .assign(year=crime.REPORTED_DATE.dt.year,
              day=crime.REPORTED_DATE.dt.day_name())
      .pipe(lambda df_ : pd.crosstab(df_.year,df_.day))
)

print((crime
            .groupby([crime['REPORTED_DATE'].dt.year.rename('year'),
                    crime['REPORTED_DATE'].dt.day_name().rename('day')])
            .size()
            .unstack('day')
            .pipe(update_2017)
            .reindex(columns=days)
)/den_100k)

days = ['Monday','Tuesday','Wednesday','Thursday',
        'Friday','Saturday','Sunday']
crime_type = 'auto-theft'
normalized = (crime.query('OFFENSE_CATEGORY_ID == @crime_type')
              .groupby([crime['REPORTED_DATE'].dt.year.rename('year'),
                       crime['REPORTED_DATE'].dt.day_name().rename('day')])
              .size()
              .unstack('day')
              .pipe(update_2017)
              .reindex(columns=days)
              .div(den_100k,axis='index')
              .astype(int)
              )
print(normalized)