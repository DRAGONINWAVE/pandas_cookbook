import pandas as pd 
import numpy  as np
import matplotlib.pyplot as plt


flights = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\flights.csv')
print(flights)
cols = ['DIVERTED','CANCELLED','DELAYED']
#print(flights
#      .assign(DELAYED=flights['ARR_DELAY'].ge(15).astype(int),
#              ON_TIME=lambda df_:1-df_[cols].any(axis=1))
#      .select_dtypes(int)
#      .sum()
#)

fig,ax_array = plt.subplots(2,3,figsize=(18,8))
(ax1,ax2,ax3),(ax4,ax5,ax6) = ax_array
fig.suptitle('2015 US Flights - Univariate Summary',size=20)
ac= flights['AIRLINE'].value_counts()
ac.plot.barh(ax=ax1,title='Airline')
(flights['ORG_AIR']
 .value_counts()
 .plot.bar(ax=ax2,rot=0,title='Origin City')
)
(flights['DEST_AIR']
 .value_counts()
 .head(10)
 .plot.bar(ax=ax3,rot=0,title='Destination City'))
(flights.assign(DELAYED=flights['ARR_DELAY'].ge(15).astype(int),
                ON_TIMR=lambda df_:1-df_[cols].any(axis=1))[['DIVERTED','CANCELLED','DELAYED']]
         .sum()
         .plot.bar(ax=ax4,rot=0,
                   log=True,title='Flight Status')
)

flights['DIST'].plot.kde(ax=ax5,xlim=(0,3000),
                         title='Distance KDE')
flights['ARR_DELAY'].plot.hist(ax=ax6,
                                 title='Arrival Delay',
                                 range=(0,2000))
fig.savefig('c12-unil.png')

df_date = (flights[['MONTH','DAY']]
           .assign(YEAR=2015,
                   HOUR=flights['SCHED_DEP']//100
                   ,MINUTE=flights['SCHED_DEP']%100))
print(df_date)

flight_dep = pd.to_datetime(df_date)
print(flight_dep)

flights.index = flight_dep
fc = flights.resample('W').size()
fc.plot.line(figsize=(12,3),title='Flight per Week',
             grid=True)
fig.savefig('c13-ts1.png')

def interp_lt_n(df_,n=600):
    return (df_.where(df_>n)
                      .interpolate(limit_direction='both'))

fig,ax = plt.subplots(figsize=(16,4))
data = (flights.resample('W')
        .size())

(data.pipe(interp_lt_n)
 .iloc[1:-1]
 .plot.line(color='black',ax=ax))

mask =data<600
(data.pipe(interp_lt_n)[mask]
 .plot.line(color='.8',linewidth=10))

ax.annotate(xy=(.8,.55),xytext=(.8,.77),
            xycoords='axes fraction',text='missing data',
            ha='center',size=20,arrowprops=dict())
ax.set_title('Flights per Week (interpolated Missing Data)')
fig.savefig('c13-ts2.png')


fig,ax = plt.subplots(figsize=(16,4))
(flights.groupby('DEST_AIR')
 ['DIST']
 .agg(['mean','count'])
 .query('count > 100')
 .sort_values('mean')
 .tail(10)
 .plot.bar(y='mean',rot=0,legend=False,ax=ax,
           title='Average Distance per Destination')
 )
fig.savefig('c13-nar1.png')

fig,ax = plt.subplots(figsize=(8,6))
(flights.reset_index(drop=True)
 [['DIST','AIR_TIME']]
 .query('DIST <= 2000')
 .dropna()
 .plot.scatter(x='DIST',y='AIR_TIME',ax=ax,alpha=.1,s=1)
 )

fig.savefig('c13-scat1.png')