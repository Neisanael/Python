
with open("./FileHandling/file.txt", "w") as file:
    file.write("HELLOW WORLD\n")
with open("./FileHandling/file.txt", "r") as file:
    file_contents = file.read()
    print(file_contents)

file = open("./FileHandling/file.txt", "w")
file.write("HAI")
file.close()

fileOpened = open("./FileHandling/file.txt", "r")
fileData = fileOpened.read()
print(fileData)
fileOpened.close()

# kalau pakai with tidak harus disertakan file.close()
# kalau menggunakan variabel harus menggunakan file.close() 
# with as auto handling close function sedangkan variabel tidak 
# direkomendasikan untuk menggunakan with sehingga program tidak rentan terhadap variabel open yang belum di close