import pandas as pd
stocks_2016 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\stocks_2016.csv'
                          ,index_col='Symbol')
stocks_2017 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\stocks_2017.csv'
                          ,index_col='Symbol')
print(stocks_2016)
print(stocks_2017)
s_list = [stocks_2016,stocks_2017]
print(pd.concat(s_list))

print(pd.concat(s_list,keys=['2016','2017'],
                names=['Year','Symbol']))
print(pd.concat(s_list,keys=['2016','2017'],
                axis='columns',
                names=['Year',None]))
print(stocks_2016.append(stocks_2017))