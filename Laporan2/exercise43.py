print("=====================================================================")
fetch_data = None
dict = {"C4":261.63, "D4":293.66, "E4":329.63, "F4":349.23, "G4":392.00, "A4":440.00, "B4":493.88}
print("{:<10} {:<}".format('Note', 'Frequency (Hz)'))

for value in dict.items() :
    note, freq = value
    print("{:<10} {:<10}".format(note, freq))

data = float(input("Masukan data yang akan dicari : "))
for note_freq, freq_hz in dict.items() :
    if data == freq_hz :
        fetch_data = note_freq
 
if fetch_data is None :
    print("Null data Fecthed")
    quit()
else :
    print("The Note is ", fetch_data)
print("=====================================================================")