from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(r'D:\python3.10\Pandas-Cookbook-master\data\chinook.db')

tracks = pd.read_sql_table('tracks',engine)
print(tracks.head())