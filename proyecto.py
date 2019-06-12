# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 12:16:49 2019

@author: jukis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xd_df = pd.read_csv('vgsales.csv', sep=',')
print(xd_df.head())


xd_df.sum(axis=1, skipna=None)
columnas = xd_df.columns.values
print(columnas)


print( xd_df['Platform'].value_counts())
a=( xd_df['NA_Sales'].sum())
b=( xd_df['EU_Sales'].sum())
c=( xd_df['JP_Sales'].sum())
d=( xd_df['Other_Sales'].sum())
print(a)
print(b)
print(c)
print(d)




print( xd_df['Publisher'].value_counts())



###nintendo = xd_df['Publisher'] == "Nintendo"
###if (nintendo == True):
   ### print(xd_df['Global_Sales']) 
###nintendo = xd_df['Publisher']

Total_Sales = xd_df['NA_Sales'] + xd_df['EU_Sales'] +xd_df['JP_Sales']+ xd_df['Other_Sales']
games= xd_df['Name']
game_sold= pd.concat([games, Total_Sales], axis=1)
game_sold.columns =[ 'game', 'total_sales']
print (game_sold)
genre=xd_df['Genre']
genre_sell= pd.concat([genre, Total_Sales], axis=1)
genre_sell.columns =[ 'genre', 'total_sales']
print(genre_sell.groupby(['genre']))





###print (Total_Sales)