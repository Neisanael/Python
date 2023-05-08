class hewan :
    def __init__(self, j, n, s):
        self.jenisHewan = j
        self.namaHewan = n
        self.suaraHewan = s
    
    def getJenisHewan(self):
        return self.jenisHewan
    def setJenisHewan(self, value):
        self.jenisHewan = value

    def getNamaHewan(self):
        return self.namaHewan
    def setNamaHewan(self, value):
        self.namaHewan = value

    def getSuaraHewan(self):
        return self.suaraHewan
    def setSuaraHewan(self, value):
        self.suaraHewan = value

    def displayOutput(self):
        print(self.jenisHewan," && ", self.namaHewan," && ", self.suaraHewan)

listHewan = []
while True:
    choice = input("Masukkan Pilihan:\n[0] Keluar\n[1] Masukkan Data\n[2] Selesai Input\n")

    if choice == "0":
        print("Keluar")
        break
    elif choice == "1":
        print("Masukkan Data")
        namaHewan = input(str("Sebutkan nama hewan? : "))
        jenisHewan = input(str("Jenis Hewanya apa? : "))
        suaraHewan = input(str("Suaranya seperti apa? : "))
        hwn = hewan(namaHewan, jenisHewan, suaraHewan)
        listHewan.append(hwn)

    elif choice == "2":
        print("Selesai Input")
        for animal in listHewan:
            animal.displayOutput()
        continue
    else:
        print("Pilihan Tidak Valid. Silahkan Ulangi.")

