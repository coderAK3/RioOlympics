import pandas as pd 
import numpy as np
import datetime as DT


df = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')

#print(df['sport'])
#print(df[['sport', 'name']])

# athletic = df.where(df['sport'] == 'athletics')
# print(athletic.head())

print(df['nationality'].value_counts()[40:50])

gold = df.groupby('nationality').sum()['gold']
silver = df.groupby('nationality').sum()['silver']
bronze = df.groupby('nationality').sum()['bronze']

total_medals = gold + silver + bronze

now = pd.Timestamp(DT.datetime(2016, 10, 5, 18, 00))
print(now)

df['dob'] = pd.to_datetime(df['dob'])
df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] - np.timedelta64(100, 'Y'))
df['age'] = (now - df['dob']).astype('<m8[Y]')
print(df)
