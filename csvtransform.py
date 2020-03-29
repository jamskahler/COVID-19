import pandas as pd

df = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', na_values='') 
df = pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'])
print(df)

df.to_csv('confirmed.csv', index=False)