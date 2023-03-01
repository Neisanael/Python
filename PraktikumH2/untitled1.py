# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:33:23 2023

@author: basisdata
"""

bulan = input("Masukan nama Bulan : ")
hari = "30"
if bulan == "februari" :
    hari = "28/29"
if bulan == "april" or bulan == "june" or bulan == "september" or bulan == "november" :
    hari = "31"
print(hari)