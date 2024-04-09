import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_temp = pd.read_csv('tempYearly.csv')
df_rain = pd.read_csv('rainYearly.csv')

#print(df_temp)
#print(df_rain)

df_temp_filter = df_temp.query('Temperature > 0 & Temperature < 40')
df_rain_filter = df_rain.query('Rainfall > 0 & Rainfall < 6')
#print(df_temp_filter)
#print(df_rain_filter)

#df_temp_filter.plot.scatter(x='Year', y='Temperature', label='Temperature and Year')
#df_rain_filter.plot.scatter(x='Year', y='Rainfall', label='Rainfall and Year')
#plt.show()

df_outer_join = pd.merge(df_temp_filter, df_rain_filter, on='Year', how='outer')
#print(df_outer_join)

df_inner_join = pd.merge(df_temp_filter, df_rain_filter, on='Year', how='inner')
print(df_inner_join.sort_values(by='Temperature', ascending=False))
print(df_inner_join.sort_values(by='Rainfall', ascending=False))

#sns.set(rc={'figure.figsize':(12,6)})
sns.jointplot(data=df_inner_join, x='Rainfall', y='Temperature', kind='reg')
plt.show()
