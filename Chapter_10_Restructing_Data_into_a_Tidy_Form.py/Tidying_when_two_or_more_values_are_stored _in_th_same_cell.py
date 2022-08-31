import pandas as pd
import numpy  as np

cities = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\texas_cities.csv')
print(cities)
geolocations = cities.Geolocation.str.split(pat='. ',
                                            expand=True)
geolocations.columns = ['latitude','latitude direction',
                        'longitude','longitude direction']
geolocations = geolocations.astype({'latitude':'float',
                                    'longitude':'float'})
print(geolocations.dtypes)
print(geolocations
      .assign(city=cities['City'])
)
print(geolocations.apply(pd.to_numeric,errors='ignore'))
print(cities.Geolocation.str.split(pat=r'бу |, ',expand=True))