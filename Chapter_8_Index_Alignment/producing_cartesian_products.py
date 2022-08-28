import pandas as pd 
import numpy as np
s1 = pd.Series(index=list('aaab'),data = np.arange(4))
print(s1)
s2 = pd.Series(index=list('cababb'),data=np.arange(6))
print(s2)
