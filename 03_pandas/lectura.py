# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:30:03 2019

@author: jukis
"""

import pandas as pd
import numpy as np
import os
import sqlite3

df = pd.read_csv("vgsales.csv")


df.to_excel('ejemplo.xlsx')
df.to_excel('ejemplo_sin_indices.xlsx', index=False)



# Multiples hojas de trabajos (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx',
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')

df.to_excel(writer, sheet_name = 'Preview Dos', index=False)

df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)

writer.save()

# Formateo Condicional
#####
artistas_contados = df['Name'].value_counts()

writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': '2_color_scale',
        'criteria': '=',
        'value': 'percentile',
        'max_value': '99',
        'max_type': 'percentile'
        }

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()



####



with  sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('Alguien', conexion)
    
###with  sqlite3.connect('bdd_python.db') as conexion:
   ### df.to_sql('Alguien', conexion)

### JSON
