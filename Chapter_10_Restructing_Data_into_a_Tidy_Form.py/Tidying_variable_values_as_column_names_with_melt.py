import pandas as pd
import numpy  as np

state_fruit2 = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\state_fruit2.csv')
print(state_fruit2)
print(state_fruit2.melt(id_vars=['State'],
                        value_vars=['Apple','Orange','Banana'])
      )
print(state_fruit2.melt(id_vars=['State'],
                        value_vars=['Apple','Orange','Banana'],
                        var_name='Fruit',
                        value_name='Weight')
      )
print(state_fruit2.melt())
print(state_fruit2.melt(id_vars='State'))