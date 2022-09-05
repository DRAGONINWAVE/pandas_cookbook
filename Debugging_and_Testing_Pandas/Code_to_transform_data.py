import pandas as pd
import numpy  as np
import zipfile
url = r'D:\python3.10\Pandas-Cookbook-master\data\kaggle-survey-2018.zip'

with zipfile.ZipFile(url) as z:
    print(z.namelist())
    kag = pd.read_csv(z.open('multipleChoiceResponses.csv'))
    df = kag.iloc[1:]
    ['multipleChoiceResponses.csv','freeFormResponses.csv',
     'SurveySchema.csv']

print(df.T)
print(df.dtypes)
print(df.Q1.value_counts(dropna=False))

def tweak_kag(df):
    na_mask = df.Q9.isna()
    hide_mask = df.Q9.str.startswith('I do not').fillna(False)
    df = df[~na_mask & ~hide_mask]

    q1 =(df.Q1
         .replace({'Prefer not to say':'Another',
         'Prefer to self-describe':'Another'})
         .rename('Gender'))

    q2 = df.Q2.str.slice(0,2).astype(int).rename('Age')
    def limit_countries(val):
        if val in {'United States of America','India','China'}:
            return val
        return 'Another'
    q3 = df.Q3.apply(limit_countries).rename('Country')

    q4 = (df.Q4
          .replace({"master's degree":18,
                    "Bachelor's degree":16,
                    "Doctoral degree":20,
                    "Some college/university study without earning a bachelor's degree":13,
                    "Professional degree":19,
                    "I prefer not to answer":None,
                    "No formal education past high school":12})
          .fillna(11)
          .rename('Edu'))
    def only_cs_stat_val(val):
        if val not in {'cs','eng','stat'}:
            return 'another'
        return val

    q5 = (df.Q5
          .replace({
              'Computer science (software engineering,etc.)':'cs',
              'Engineering(non-computer focused)':'eng',
              'Mathmatics or statistucs':'stat'})
          .apply(only_cs_stat_val)
          .rename('Studies'))

    def limit_occupation(val):
        if val in {'Student','Data Scientist','Software Engineer','Not employed',
                   'Data Engineer'}:
            return val
        return 'Another'

    q6 = df.Q6.apply(limit_occupation).rename('Occupation')

    q8 = (df.Q8
          .str.replace('+','')
          .str.split('-',expand=True)
          .iloc[:,0]
          .fillna(-1)
          .astype(int)
          .rename('Experience')
          )

    q9 = (df.Q9
          .str.replace('+','')
          .str.replace(',','')
          .str.replace('500000','500')
          .str.replace('I do not wish disclose my approximate yearly compensation','')
          .str.split('-',expand=True)
          .iloc[:,0]
          .astype(int)
          .mul(1000)
          .rename('Salary'))
    return pd.concat([q1,q2,q3,q4,q5,q6,q8,q9],axis=1)

print(tweak_kag(df))
print(tweak_kag(df).dtypes)

kag = tweak_kag(df)
print(kag
      .groupby('Country')
      .apply(lambda g : g.Salary.corr(g.Experience)))