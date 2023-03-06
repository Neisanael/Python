print("=====================================================================")
bulan = input("Masukan nama Bulan : ")
hari = "30"
if bulan == "februari" :
    hari = "28/29"
if bulan == "april" or bulan == "june" or bulan == "september" or bulan == "november" :
    hari = "31"
print(hari)
print("=====================================================================")