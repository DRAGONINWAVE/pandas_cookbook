from cgitb import text
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

meetup = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\meetup_groups.csv',
                     parse_dates=['join_date'],
                     index_col='join_date')
print(meetup)
print(meetup
      .groupby([pd.Grouper(freq='W'),'group'])
      .size()
)
print(meetup
      .groupby([pd.Grouper(freq='W'),'group'])
      .size()
      .unstack('group',fill_value=0)
)
print(meetup
      .groupby([pd.Grouper(freq='W'),'group'])
      .size()
      .unstack('group',fill_value=0)
      .cumsum()
)
print(meetup
      .groupby([pd.Grouper(freq='W'),'group'])
      .size()
      .unstack('group',fill_value=0)
      .cumsum()
      .pipe(lambda df_:df_.div(
          df_.sum(axis='columns'),axis='index'))
)

fig,ax = plt.subplots(figsize=(18,6))
(meetup
 .groupby([pd.Grouper(freq='W'),'group'])
 .size()
 .unstack('group',fill_value=0)
 .cumsum()
 .pipe(lambda df_:df_.div(
     df_.sum(axis='columns'),axis='index'))
 .plot.area(ax=ax,
            cmap='Greys',xlim=('2013-6',None),
            ylim=(0,1),legend=False)
 )
ax.figure.suptitle('Houston Meetup Groups',size=25)
ax.set_xlabel('')
ax.yaxis.tick_right()
kwargs = {'xycoords':'axes fraction','size':15}
ax.annotate(xy=(.1,.7),text='R Users',
            color='w',**kwargs)
ax.annotate(xy=(.25,.16),text='Date Visualization',
            color='k',**kwargs)
ax.annotate(xy=(.5,.55),text='Energy Data Science',
            color='k',**kwargs)
ax.annotate(xy=(.83,.07),text='Data Science',
            color='k',**kwargs)
ax.annotate(xy=(.86,.78),text='Machine Learning',
            color='k',**kwargs)
fig.savefig('c13-stacked1.png')