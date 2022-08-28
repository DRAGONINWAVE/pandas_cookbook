from enum import unique
from random import random
import pandas as pd
import numpy  as np

college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv',
                      index_col='INSTNM')
print(college.dtypes)
print(college.MD_EARN_WNE_P10.sample(10,random_state=42))
print(college.MD_EARN_WNE_P10.value_counts())
print(college.GRAD_DEBT_MDN_SUPP.value_counts())
print(college.GRAD_DEBT_MDN_SUPP.sample(10,random_state=42))

cols = ['MD_EARN_WNE_P10','GRAD_DEBT_MDN_SUPP']
for col in cols:
    college[col] = pd.to_numeric(college[col],errors='coerce')
print(college.dtypes.loc[cols])
college_n = college.select_dtypes('number')
print(college_n.head())
binary_only = college_n.nunique() == 2
print(binary_only.head())
binary_cols = binary_only[binary_only].index
print(binary_cols)
college_n2 = college_n.drop(columns=binary_cols)
print(college_n2.head())
max_cols = college_n2.idxmax()
print(max_cols)
unique_max_cols = max_cols.unique()
print(unique_max_cols[:5])
print(college_n2.loc[unique_max_cols].style.highlight_max())