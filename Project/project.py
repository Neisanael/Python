import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('Projects.xlsx', sheet_name='Sheet1')

class Grade:
    def __init__(self, name, nim, sdnl, platform, rpl, imk, asa, pad, kompardis, ips):
        self.name = name
        self.nim = nim
        self.sdnl = sdnl
        self.platform = platform
        self.rpl = rpl
        self.imk = imk
        self.asa = asa
        self.pad = pad
        self.kompardis = kompardis
        self.ips = ips

class App:
    def __init__(self, root):
        # setting title
        root.title("Nilai Mahasiswa")
        # setting window size
        width = 610
        height = 70
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ButtonTertinggi = tk.Button(root)
        ButtonTertinggi["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        ButtonTertinggi["font"] = ft
        ButtonTertinggi["fg"] = "#000000"
        ButtonTertinggi["justify"] = "center"
        ButtonTertinggi["text"] = "Nilai Tertinggi"
        ButtonTertinggi.place(x=10, y=20, width=100, height=25)
        ButtonTertinggi["command"] = self.ButtonTertinggi_command

        ButtonTerendah = tk.Button(root)
        ButtonTerendah["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        ButtonTerendah["font"] = ft
        ButtonTerendah["fg"] = "#000000"
        ButtonTerendah["justify"] = "center"
        ButtonTerendah["text"] = "Nilai Terendah"
        ButtonTerendah.place(x=120, y=20, width=100, height=25)
        ButtonTerendah["command"] = self.ButtonTerendah_command

        ButtonRata = tk.Button(root)
        ButtonRata["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        ButtonRata["font"] = ft
        ButtonRata["fg"] = "#000000"
        ButtonRata["justify"] = "center"
        ButtonRata["text"] = "Nilai Rata Rata"
        ButtonRata.place(x=230, y=20, width=100, height=25)
        ButtonRata["command"] = self.ButtonRata_command

        ButtonTampil = tk.Button(root)
        ButtonTampil["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        ButtonTampil["font"] = ft
        ButtonTampil["fg"] = "#000000"
        ButtonTampil["justify"] = "center"
        ButtonTampil["text"] = "Tampilkan Data"
        ButtonTampil.place(x=340, y=20, width=100, height=25)
        ButtonTampil["command"] = self.ButtonTampil_command

        ButtonClear = tk.Button(root)
        ButtonClear["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        ButtonClear["font"] = ft
        ButtonClear["fg"] = "#000000"
        ButtonClear["justify"] = "center"
        ButtonClear["text"] = "Clear"
        ButtonClear.place(x=530, y=20, width=70, height=25)
        ButtonClear["command"] = self.ButtonClear_command

        ButtonGraph = tk.Button(root)
        ButtonGraph["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        ButtonGraph["font"] = ft
        ButtonGraph["fg"] = "#000000"
        ButtonGraph["justify"] = "center"
        ButtonGraph["text"] = "Graph IPS"
        ButtonGraph.place(x=450, y=20, width=70, height=25)
        ButtonGraph["command"] = self.ButtonGraph_command

    def read_excel_data(self):
        df = pd.read_excel('...Project...xlsx', sheet_name='Sheet1')
        for _, row in df.iterrows():
            grade = Grade(
                name=row['Nama'],
                nim=row['Nim'],
                sdnl=row['SDNL'],
                platform=row['Platform'],
                rpl=row['RPL'],
                imk=row['IMK'],
                asa=row['ASA'],
                pad=row['PAD'],
                kompardis=row['Kompardis'],
                ips=row['IPS']
            )
            self.grades.append(grade)

    def ButtonTertinggi_command(self):
        if not self.grades:
            self.read_excel_data()
        max_ipk = np.max(grade.ips for grade in self.grades)
        print(f"Nilai Tertinggi IPK: {max_ipk}")
        print(np.max(df['IPS']))

    def ButtonTerendah_command(self):
        print(np.min(df['IPS']))

    def ButtonRata_command(self):
        print(np.mean(df['IPS']))

    def ButtonTampil_command(self):
        print("command")

    def ButtonClear_command(self):
        print("command")

    def ButtonGraph_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
