# this database does not have dates, the csv file is directly downloaded from the site

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('weather_data.csv')

print('First 10 rows')
print(f'{df.head(10)}\n')

print(f'Shape of dataset {df.shape}\n')
print(f'{df.describe()} \n')

print(f'{df.dtypes}\n')

# replacing missing values with the average value of the corresponding column
for column in df.columns:
    average = df[column].mean()
    weather = df.replace({column: {np.nan: average}})

# there is no date column, but below would be the code if there were.
df['date'] = pd.to_datetime(df['date'])

#average temperature and humidity by month

mo_averages = df.groupby(['year','month']).agg({'temperature': 'mean', 'humidity': 'mean'})

#temp line plot
plt.plot(mo_averages['month'], mo_averages['temperatures'])
plt.plot(mo_averages['month'], mo_averages['humidity'])

#labeling x and y axis for the visualization
plt.xlabel('Month') 
plt.ylabel('Ave rage')
plt.show()

# month with highest and lowest wind speeds
# also not in dataset 

wind_avg = df.groupby(['year', 'month']).agg({'wind_speed'})

# finding months with lowest and highest speed averages
max_speed = wind_avg.loc[wind_avg['wind_speed'].idmax()]
min_speed = wind_avg.loc[wind_avg['wind_speed'].idmin()]

#use seaborn for histogram
plt.hist(df['wind_speed'])
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')
plt.show()

