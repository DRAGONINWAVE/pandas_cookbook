import pandas as pd
import numpy  as np

weightlifting = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\weightlifting_men.csv')
print(weightlifting)
print(weightlifting
      .melt(id_vars='Weight Category',
            var_name='sex_age',
            value_name='Qual Total')
)
print(weightlifting
      .melt(id_vars='Weight Category',
            var_name='sex_age',
            value_name='Qual Total')
      ['sex_age']
      .str.split(expand=True)
      .rename(columns={0:'Sex',1:'Age Group'})
)
print(weightlifting
      .melt(id_vars='Weight Category',
            var_name='sex_age',
            value_name='Qual Total')
      ['sex_age']
      .str.split(expand=True)
      .rename(columns={0:'Sex',1:'Age Group'})
      .assign(Sex=lambda df_:df_.Sex.str[0])
)
melted = (weightlifting
          .melt(id_vars='Weight Category',
                var_name='sex_age',
                value_name='Qual Total')
)
tidy = pd.concat([melted['sex_age']
                  .str.split(expand=True)
                  .rename(columns={0:'Sex',1:'Age Group'})
                  .assign(Sex=lambda df_:df_.Sex.str[0]),
                  melted[['Weight Category','Qual Total']]],
                 axis='columns')
print(tidy)
print(melted['sex_age']
      .str.split(expand=True)
      .rename(columns={0:'Sex',1:'Age Group'})
      .assign(Sex=lambda df_:df_.Sex.str[0]
              ,Category=melted['Weight Category'],
              Total=melted['Qual Total'])
)
tidy2 = (weightlifting
         .melt(id_vars='Weight Category',
               var_name='sex_age',
               value_name='Qual Total')
         .assign(Sex=lambda df_:df_.sex_age.str[0],
                 **{'Age Group':(lambda df_:(df_
                                             .sex_age
                                             .str.extract(r'(\d{2}[-+](?:\d{2})?)',
                                                          expand=False)))})
         .drop(columns='sex_age')
         )
print(tidy2)
print(tidy.sort_index(axis=1).equals(tidy2.sort_index(axis=1)))