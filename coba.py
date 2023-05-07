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
    
hewan1 = hewan("Anjing", "Blacky", "Whoof")
hewan1.displayOutput()
hewan1.setJenisHewan("Kucing")
hewan1.displayOutput()
