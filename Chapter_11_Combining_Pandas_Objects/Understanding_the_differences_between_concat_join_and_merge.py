import pandas as pd
import numpy  as np

years = 2016,2017,2018
stock_tables = [pd.read_csv(
    f'D:\python3.10\Pandas-Cookbook-master\data\stocks_{year}.csv',index_col='Symbol')
                for year in years]
stocks_2016,stocks_2017,stocks_2018 = stock_tables
print(stocks_2016)
print(pd.concat(stock_tables,keys=[2016,2017,2018]))
print(pd.concat(dict(zip(years,stock_tables)),axis='columns'))
print(stocks_2016.join(stocks_2017,lsuffix='_2016',
                       rsuffix='_2017',how='outer'))
other = [stocks_2017.add_suffix('_2017'),
         stocks_2018.add_suffix('_2018')]
print(stocks_2016.add_suffix('_2016').join(other,how='outer'))

stock_join = stocks_2016.add_suffix('_2016').join(other,how='outer')
stock_concat = (
    pd.concat(
        dict(zip(years,stock_tables)),axis='columns')
    .swaplevel(axis=1)
    .pipe(lambda df_:
          df_.set_axis(df_.columns.to_flat_index(),axis=1))
    .rename(lambda label:
            '_'.join([str(x) for x in label]),axis=1)
)
print(stock_join.equals(stock_concat))

print(stocks_2016.merge(stocks_2017,left_index=True,
                 right_index=True))
stock_merge = (stocks_2016
               .merge(stocks_2017,left_index=True,
                      right_index=True,how='outer',
                      suffixes=('_2016','_2017'))
               .merge(stocks_2018.add_suffix('_2018'),
                      left_index=True,right_index=True,
                      how='outer')
               )
print(stock_concat.sort_index().equals(stock_merge))
names = ['prices','transactions']
food_tables = [pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\food_{}.csv'.format(name))for name in names]
food_prices,food_transactions = food_tables
print(food_prices)
print(food_transactions)
print(food_transactions.merge(food_prices,on=['item','store']))
print(food_transactions.merge(food_prices.query('Date == 2017'),
                              how='left'))
food_prices_join = food_prices.query('Date == 2017').set_index(['item','store'])
print(food_prices_join)
print(food_transactions.join(food_prices_join,on=['item','store']))