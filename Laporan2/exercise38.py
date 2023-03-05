name = None
dict = {3:"Triangle", 4:"Quadrangle", 5:"Pentagon", 6:"Hexagon", 7:"Heptagon", 8:"Octagon", 9:"Nonagon", 10:"Decagon"}
print("=====================================================================")
sisi = int(input("masukan jumlah sisi : "))

for item in dict.keys() :
    if sisi == item :
        name = dict.get(item)

if name is None :
    print("No data name Found!")
else :
    print("The shape name is : ",name)
print("=====================================================================")