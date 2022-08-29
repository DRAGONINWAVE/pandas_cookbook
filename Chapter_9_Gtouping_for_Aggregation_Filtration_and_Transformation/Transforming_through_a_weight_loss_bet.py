import pandas as pd
import numpy  as np

weight_loss = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\weight_loss.csv')
print(weight_loss.query('Month=="Jan"'))

def percent_loss(s):
    return ((s - s.iloc[0]) / s.iloc[0]) * 100

print(
    weight_loss
    .query('Name=="Bob" and Month == "Jan"')
    ['Weight']
    .pipe(percent_loss)
    )

print(
    weight_loss
    .groupby(['Name','Month'])
    ['Weight']
    .transform(percent_loss)
    )