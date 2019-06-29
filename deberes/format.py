# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:41:06 2019

@author: jukis
"""

import pandas as pd
import numpy as np 
import xlsxwriter as xls


data = pd.read_csv("vgsales.csv")




genero = data['Genre'].value_counts()
writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')
genero.to_excel(writer, sheet_name = 'Generos contados')
hoja_generos = writer.sheets['Generos contados']
rangos_celdas = 'B2:B{}'.format(len(genero.index)+1)

formato = {
        'type' : '2_color_scale',
        'min_value' : '10',
        'min_type' : 'percentile',
        'min value': '99',
        'max_type' : 'percentile'
        }
hoja_generos.conditional_format(rangos_celdas,formato)
writer.save()
