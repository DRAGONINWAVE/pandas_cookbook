import pandas as pd 
import numpy  as np

flights = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\flights.csv')
print(flights)
bins = [-np.inf,200,500,1000,2000,np.inf]
cuts = pd.cut(flights['DIST'],bins=bins)
print(cuts)
print(cuts.value_counts())
print(flights.groupby(cuts)['AIRLINE']
      .value_counts(normalize=True)
      .round(3)
)
print(
    flights.groupby(cuts)
    ['AIR_TIME']
    .quantile(q=[.25,.5,.75])
    .div(60)
    .round(2))

labels = ['Under an Hour','1 Hour','1-2 Hours','2-4 Hours','4+ Hours']
cuts2 = pd.cut(flights['DIST'],bins=bins,labels=labels)
print(
    flights.groupby(cuts2)
    ['AIRLINE']
    .value_counts(normalize=True)
    .round(3)
    .unstack()
)
