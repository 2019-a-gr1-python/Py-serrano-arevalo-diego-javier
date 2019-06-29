# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:19:39 2019

@author: jukis
"""
import scrapy 
import numpy as np

nombre_producto = response.css('.product-tile-inner > .name::text').extract()
nombre_producto = np.array(nombre_producto)
nombre_producto

precio = list(map(lambda x: x.split(')')[0][12:] , response.css('div.side > div.price::attr(data-bind)').extract()))
precio = np.array(precio,dtype='float32')

precio_descuento = list( map(lambda x: x.split(')')[0][12:],response.css('div.price-member > div::attr(data-bind)').extract()))
precio_descuento = np.array(precio_descuento,dtype='float32')
descuentos = precio - precio_descuento

descuentos

producto_mas_descuento = nombre_producto[descuentos==descuentos.max()]
producto_mas_descuento

