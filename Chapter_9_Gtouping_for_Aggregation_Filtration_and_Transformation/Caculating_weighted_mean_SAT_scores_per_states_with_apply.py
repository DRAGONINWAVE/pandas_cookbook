import pandas as pd
import numpy as np
from scipy.stats import gmean,hmean

college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv')
subset = ['UGDS','SATMTMID','SATVRMID']
college2 = college.dropna(subset=subset)
print(college.shape)
print(college2.shape)

def weighted_math_average(df):
    weighted_math = df['UGDS'] * df['SATMTMID']
    return int(weighted_math.sum() / df['UGDS'].sum())

#college2 = college2.groupby('STABBR').apply(weighted_math_average)
#print(college2)

def weighted_average(df):
    weight_m = df['UGDS'] * df['SATMTMID']
    weight_v = df['UGDS'] * df['SATVRMID']
    wm_avg = weight_m.sum() / df['UGDS'].sum()
    wv_avg = weight_v.sum() / df['UGDS'].sum()
    data = {'w_math_avg':wm_avg,
            'w_verbal_avg':wv_avg,
            'math_avg':df['SATMTMID'].mean(),
            'verbal_avg':df['SATVRMID'].mean(),
            'count':len(df)}
    return pd.Series(data)

print(college2
      .groupby('STABBR')
      .apply(weighted_average)
      .astype(int))

def calculate_means(df):
    df_means = pd.DataFrame(index=['Arithmetic','Weighted','Geometric','Harmonic'])
    cols = ['SATMTMID','SATVRMID']
    for col in cols:
        arithmetic = df[col].mean()
        weighted = np.average(df[col],weights=df['UGDS'])
        geometric = gmean(df[col])
        harmonic = hmean(df[col])
        df_means[col] = [arithmetic,weighted,geometric,harmonic]
    df_means['count'] = len(df)
    return df_means.astype(int)
print(college2.groupby('STABBR')
      .apply(calculate_means)
      )