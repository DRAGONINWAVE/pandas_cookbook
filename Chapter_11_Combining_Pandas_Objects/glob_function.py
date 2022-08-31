import pandas as pd
import numpy  as np
import glob

df_list = []
for filename in glob.glob(r'D:\python3.10\Pandas-Cookbook-master\data\gas prices\*.csv'):
    df_list.append(pd.read_csv(filename,index_col='Week',
                               parse_dates=['Week']))
gas = pd.concat(df_list,axis='columns')
print(gas)


