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

print(
    weight_loss
    .assign(percent_loss=(weight_loss
                          .groupby(['Name','Month'])
                          ['Weight']
                          .transform(percent_loss)
                          .round(1)))
    .query('Name=="Bob" and Month in ["Jan","Feb"]')
    )


print(
    weight_loss
    .assign(percent_loss=(weight_loss
                          .groupby(['Name','Month'])
                          ['Weight']
                          .transform(percent_loss)
                          .round(1)))
    .query('Week == "Week 4"')
    )
print(
    weight_loss
    .assign(percent_loss=(weight_loss
                                     .groupby(['Name','Month'])
                                     ['Weight']
                                     .transform(percent_loss)
                                     .round(1)))
    .query('Week == "Week 4"')
    .pivot(index='Month',columns='Name',
           values='percent_loss')
    )

print(weight_loss
      .assign(percent_loss=(weight_loss
                             .groupby(['Name','Month'])
                             ['Weight']
                             .transform(percent_loss)
                             .round(1)))
      .query('Week == "Week 4"')
      .pivot(index='Month',columns='Name',
             values='percent_loss')
      .assign(winner=lambda df_:
              np.where(df_.Amy < df_.Bob,'Amy','Bob'))
      )
print(weight_loss
      .assign(percent_loss=(weight_loss
                             .groupby(['Name','Month'])
                             ['Weight']
                             .transform(percent_loss)
                             .round(1)))
      .query('Week == "Week 4"')
      .pivot(index='Month',columns='Name',
             values='percent_loss')
      .assign(winner=lambda df_:
              np.where(df_.Amy < df_.Bob,'Amy','Bob'))
      .style.highlight_min(axis=1)
      )