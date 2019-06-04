# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 07:11:25 2019

@author: jukis
"""

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('titanic.csv')
df.head()
print (df.shape)
print (df.count)

col_names = df.columns.tolist()

for column in col_names:
    print ("Valores nulos en <{0}>: {1} ".format(column, df[column].isnull().sum()))

d = {'male' : 'M' , 'female' : 'F' }
df['Sex'] = df['Sex'].apply(lambda x:d[x])

df['Sex'].head()

print( df.describe())

print (df[df.Fare==0])

print(pd.crosstab(df.Survived, df.Sex))

pclass_gender_survival_count_df = df.groupby(['Pclass', 'Sex'] ) ['Survived'].sum()
print(pclass_gender_survival_count_df)

fig = plt.figure(figsize=(30,10)) 
plt.subplot2grid((2,3),(0,0))
df.Survived.value_counts().plot(kind ='bar', alpha=0.5)
plt.title('Sobrevivientes total')

plt.subplot2grid((2,3),(0,1))
df.Survived.value_counts(normalize = True).plot(kind ='bar', alpha=0.5)
###
fig = plt.figure(figsize=(10,5))
df.Sex[df.Survived==1].value_counts(normalize = True).plot(kind ='bar', alpha=0.5)

plt.title('Sobrevivieron Male vs Female')
plt.show

fig = plt.figure(figsize=(10,5))
df.Pclass[df.Survived == 1].value_counts(normalize = True).plot(kind='bar', alpha=0.5)
plt.title('Sobrevivientes por Clase de Ticket')
plt.show(fig)


fig = plt.figure(figsize=(20,10))
for t_class in [1,2,3]:
    df.Age[df.Pclass == t_class].plot(kind='kde')
plt.legend(("1era Clase", "2nda Clase", "3era clase"))
plt.show()


















