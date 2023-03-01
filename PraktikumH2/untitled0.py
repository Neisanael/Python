# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:30:15 2023

@author: basisdata
"""

sisi = int(input("masukan jumlah sisi : "))
if sisi == 3 :
    name = "triangle"
if sisi == 4 :
    name = "quadrilateral"
if sisi == 5 :
    name = "pentagon"
if sisi == 6 :
    name = "hexagon"
if sisi == 7 :
    name = "neptagon"
if sisi == 8 :
    name = "octagon"
if sisi == 9 :
    name = "nonagon"
if sisi == 10 :
    name = "decagon"
print(name)