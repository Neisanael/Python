sisi1 = int(input("Masukan panjang sisi 1 : "))
sisi2 = int(input("Masukan panjang sisi 2 : "))
sisi3 = int(input("Masukan panjang sisi 3 : "))

if sisi1 == sisi2 == sisi3 :
    segi = "Segitiga Sama sisi"
elif sisi1 == sisi2 != sisi3 or sisi2 == sisi3 != sisi1 or sisi3 == sisi1 != sisi2 :
    segi = "Segitiga sama kaki"
else :
    segi = "Segitiga Sembarang"
print(segi)