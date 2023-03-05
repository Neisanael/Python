import math
number = None
dict = {"C4":261.63, "D4":293.66, "E4":329.63, "F4":349.23, "G4":392.00, "A4":440.00, "B4":493.88}
print("{:<10} {:<}".format('Note', 'Frequency (Hz)'))

for value in dict.items() :
    note, freq = value
    print("{:<10} {:<10}".format(note, freq))

data = str(input("Masukan data yang akan dicari : "))
for item in dict.keys() :
    if data == item :
        number = dict.get(item)

if number is None :
    quit()
else :
    result = float(number) / float(math.pow(2,(4-float(number))))
    print(result)