from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///data/chinook.db')
tracks = pd.read_sql_table('tracks',engine)
print()