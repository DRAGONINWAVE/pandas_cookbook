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

print(flights
      .reset_index(drop=True)
      [['DIST','AIR_TIME']]
      .query('DIST <= 2000')
      .dropna()
      .pipe(lambda df_:pd.cut(df_.DIST,
                              bins=range(0,2001,250)))
      .value_counts()
      .sort_index()
      )

zscore = lambda x:(x-x.mean())/x.std()
short = (flights[['DIST','AIR_TIME']]
         .query('DIST <= 2000')
         .dropna()
         .reset_index(drop=True)
         .assign(BIN=lambda df_:pd.cut(df_.DIST,bins=range(0,2001,250))))

scores = short.groupby('BIN')['AIR_TIME'].transform(zscore)

print(short.assign(SCORE=scores))

fig,ax = plt.subplots(figsize=(10,6))
short.assign(SCORE=scores).pivot(columns='BIN')['SCORE'].plot.box(ax=ax)
ax.set_title('Z-Score for Distance Groups')
fig.savefig('c13-box2.png')

mask = (short.assign(SCORE=scores)
        .pipe(lambda df_:df_.SCORE.abs() >6)
)

outliers = (flights[['DIST','AIR_TIME']]
            .query('DIST <= 2000')
            .dropna()
            .reset_index(drop=True)
            [mask]
            .assign(PLOT_NUM=lambda df_:range(1,len(df_)+1))
            )
print(outliers)

fig,ax = plt.subplots(figsize=(8,6))
(short
 .assign(SCORE=scores)
 .plot.scatter(x='DIST',y='AIR_TIME',
               alpha=.1,s=1,ax=ax,
               table=outliers))

outliers.plot.scatter(x='DIST',y='AIR_TIME',
                      s=25,ax=ax,grid=True)
outs = outliers[['AIR_TIME','DIST','PLOT_NUM']]
for t,d,n in outs.itertuples(index=False):
    ax.text(d+5,t+5,str(n))


plt.setp(ax.get_xticklabels(),y=.1)
plt.setp(ax.get_xticklines(),visible=False)
ax.set_xlabel('')
ax.set_title('Flight Time vs Distance with Outliers')
fig.savefig('c13-scat3.png',dpi=300,bbox_inches='tight')
