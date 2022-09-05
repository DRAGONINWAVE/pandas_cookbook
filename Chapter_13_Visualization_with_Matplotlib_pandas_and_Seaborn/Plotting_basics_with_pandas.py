import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

df = pd.DataFrame(index=['Atiya','Abbas','Cornelia',
                         'Stephanie','Monte'],
                  data={'Apples':[2,10,40,20,50],
                        'Oranges':[35,40,25,19,33]})

print(df)
color = ['.2','.7']
ax  =df.plot.bar(color=color,figsize=(16,4))
ax.get_figure().savefig('c13-pdemo-bar1.png')

ax = df.plot.kde(color = color,figsize=(16,4))
ax.get_figure().savefig('c13-pdemo-kde1.png')

fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(16,4))
fig.suptitle('Two Variable Plots',size=20,y=1.02)
df.plot.line(ax=ax1,title='Line plot')
df.plot.scatter(x='Apples',y='Oranges',
                ax=ax2,title='Scatterplot')
df.plot.bar(color=color,ax=ax3,title='Bar plot')
fig.savefig('c13-pdemo-scat.png')

fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(16,4))
fig.suptitle('Two Variable Plots',size=20,y=1.02)
df.plot.kde(color=color,ax=ax1,title='KDE plot')
df.plot.box(ax=ax2,title='Boxplot')
df.plot.hist(color=color,ax=ax3,title='Histogram')
fig.savefig('c13-pdemo-kde2.png')

fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(16,4))
df.sort_values('Apples').plot.line(x='Apples',y='Oranges',
                                   ax=ax1)
df.plot.bar(x='Apples',y='Oranges',ax=ax2)
df.plot.kde(x='Apples',ax=ax3)
fig.savefig('c13-pdemo-kde.png')