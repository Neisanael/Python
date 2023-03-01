# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:42:18 2023

@author: basisdata
"""
import math
dict = {"C4":261.63, "D4":293.66, "E4":329.63, "F4":349.23, "G4":392.00, "A4":440.00, "B4":493.88}
print(dict)

data = str(input("Masukan data yang akan dicari : "))
for item in dict.keys() :
    if data == item :
        number = dict.get(item)
        
saved_data = number
print(saved_data)
result = float(saved_data) / float(math.pow(2,(4-float(saved_data))))
print(result)