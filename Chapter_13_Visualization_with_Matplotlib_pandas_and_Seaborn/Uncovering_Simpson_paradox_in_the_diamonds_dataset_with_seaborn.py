import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.cm import Greys

dia = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\diamonds.csv')
print(dia)
cut_cats = ['Fair','Good','Very Good','Premium','Ideal']
color_cats = ['J','I','H','G','F','E','D']
clarity_cats = ['I1','SI2','SI1','VS2',
                'VS1','VVS2','VVS1','IF']
dia2 = (dia
        .assign(cut=pd.Categorical(dia['cut'],
                                   categories=cut_cats,
                                   ordered=True),
                color=pd.Categorical(dia['color'],
                                     categories=color_cats,
                                     ordered=True),
                clarity=pd.Categorical(dia['clarity'],
                                       categories=clarity_cats,
                                       ordered=True))
)
print(dia2)


fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(14,4))
sns.barplot(x='color',y='price',data=dia2,ax=ax1)
sns.barplot(x='cut',y='price',data=dia2,ax=ax2)
sns.barplot(x='clarity',y='price',data=dia2,ax=ax3)
fig.suptitle('Price Decreasing with Increasing Quality?')
fig.savefig('c13-bar4.png',dpi=300,bbox_inches='tight')

grid = sns.catplot(x='color',y='price',col='clarity',
                   col_wrap=4,data=dia2,kind='bar')
grid.fig.savefig('c13-bar5.png',dpi=300,bbox_inches='tight')

fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(14,4))
sns.barplot(x='color',y='carat',data=dia2,ax=ax1)
sns.barplot(x='cut',y='carat',data=dia2,ax=ax2)
sns.barplot(x='clarity',y='carat',data=dia2,ax=ax3)
fig.suptitle('Diamond size decreases with quality')
fig.savefig('c13-bar6.png',dpi=300,bbox_inches='tight')

dia2 = (dia2
        .assign(carat_category=pd.qcut(dia2.carat,5))
)
greys = Greys(np.arange(50,250,40))
grid = sns.catplot(x='clarity',y='price',data=dia2,
                   hue='carat_category',col='color',
                   col_wrap=4,kind='point',palette=greys)
grid.fig.suptitle('Diamond price by size,color and clarity',
                  y=1.02,size=20)
grid.fig.savefig('c13-bar7.png',dpi=300,bbox_inches='tight')

g = sns.PairGrid(dia2,height=5,
                 x_vars=['color','cut','clarity'],
                 y_vars=['price'])
g.map(sns.barplot)
g.fig.suptitle('Replication of Step 3 with PairGrid',y=1.02)
g.fig.savefig('c13-bar8.png',dpi=300,bbox_inches='tight')