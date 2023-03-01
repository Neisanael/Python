# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:37:55 2023

@author: basisdata
"""

sisi1 = int(input("Masukan panjang sisi 1 : "))
sisi2 = int(input("Masukan panjang sisi 2 : "))
sisi3 = int(input("Masukan panjang sisi 3 : "))

if sisi1 == sisi2 and sisi1 == sisi3 and sisi3 == sisi2 :
    segi = "Segitiga Sama sisi"
if sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3 :
    segi = "Segitiga sama kaki"
else :
    segi = "Segitiga Sembarang"
print(segi)