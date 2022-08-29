import pandas as pd
import numpy  as np

college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv',index_col='INSTNM')
grouped = college.groupby('STABBR')
print(grouped.ngroups)
print(college['STABBR'].nunique())

def check_minority(df,threshold):
    minority_pct = 1 - df['UGDS_WHITE']
    total_minority = (df['UGDS'] * minority_pct).sum()
    total_ugds = df['UGDS'].sum()
    total_minority_pct = total_minority / total_ugds
    return total_minority_pct > threshold

college_filtered = grouped.filter(check_minority,threshold=.5)
print(college_filtered)
print(college.shape)
print(college_filtered.shape)
print(college_filtered['STABBR'].nunique())
college_filtered_20 = grouped.filter(check_minority,threshold=.2)
print(college_filtered_20.shape)
print(college_filtered_20['STABBR'].nunique())
college_filtered_70 = grouped.filter(check_minority,threshold=.7)
print(college_filtered_70.shape)
print(college_filtered_70['STABBR'].nunique())