import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Nilai Mahasiswa")
        width = 420
        height = 60
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_161=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_161["font"] = ft
        GLabel_161["fg"] = "#333333"
        GLabel_161["justify"] = "center"
        GLabel_161["text"] = "PROJECT PAD KELOMPOK D"
        GLabel_161.place(x=120,y=0,width=200,height=25)

        ButtonChooseFile = tk.Button(self.root)
        ButtonChooseFile["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        ButtonChooseFile["font"] = ft
        ButtonChooseFile["fg"] = "#000000"
        ButtonChooseFile["justify"] = "center"
        ButtonChooseFile["text"] = "Choose File"
        ButtonChooseFile.place(x=10, y=20, width=100, height=25)
        ButtonChooseFile["command"] = self.ButtonChooseFile_command

        self.ButtonStatistik = tk.Button(self.root)
        self.ButtonStatistik["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        self.ButtonStatistik["font"] = ft
        self.ButtonStatistik["fg"] = "#000000"
        self.ButtonStatistik["justify"] = "center"
        self.ButtonStatistik["text"] = "Statistik"
        self.ButtonStatistik["command"] = self.ButtonStatistik_command
        self.ButtonStatistik.pack_forget()

        self.ButtonTampil = tk.Button(self.root)
        self.ButtonTampil["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        self.ButtonTampil["font"] = ft
        self.ButtonTampil["fg"] = "#000000"
        self.ButtonTampil["justify"] = "center"
        self.ButtonTampil["text"] = "Tampilkan Data"
        self.ButtonTampil["command"] = self.ButtonTampil_command

        self.ButtonGraph = tk.Button(self.root)
        self.ButtonGraph["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times', size=10)
        self.ButtonGraph["font"] = ft
        self.ButtonGraph["fg"] = "#000000"
        self.ButtonGraph["justify"] = "center"
        self.ButtonGraph["text"] = "Graph IPS"
        self.ButtonGraph["command"] = self.ButtonGraph_command

    def ButtonChooseFile_command(self):
        filetypes = (('excel', '*.xlsx'),)

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='C:/Users/neisanael/Documents/GitHub/Python/Project/s',
            filetypes=filetypes)

        if filename:
            showinfo(
                title='Selected File',
                message=filename
            )

            self.df = pd.read_excel(filename)
            self.ButtonTampil_command()
            self.ButtonStatistik.place(x=120, y=20, width=100, height=25)
            self.ButtonTampil.place(x=230, y=20, width=100, height=25)
            self.ButtonGraph.place(x=340, y=20, width=70, height=25)
        else:
            showinfo(
                title='No File Selected',
                message='No file was selected.')
            self.ButtonStatistik.pack_forget()

    def ButtonStatistik_command(self):
        window = tk.Toplevel(self.root)
        window.title("Statistik Nilai")
        
        columns = ["Statistik", "Value"]
        
        treeview = ttk.Treeview(window, show='headings', columns=columns)
        treeview.heading("Statistik", text="Statistik")
        treeview.heading("Value", text="Value")
        treeview.pack(fill="both", expand=True)
        
        min_value = np.min(self.df['IPS'])
        max_value = np.max(self.df['IPS'])
        mean_value = np.mean(self.df['IPS'])
        
        treeview.insert("", tk.END, values=("Min", min_value))
        treeview.insert("", tk.END, values=("Max", max_value))
        treeview.insert("", tk.END, values=("Mean", mean_value))

    def ButtonTampil_command(self):
        window = tk.Toplevel(self.root)
        window.title("Data Mahasiswa")
        columns = [col for col in self.df.columns if col != 'dtype']

        treeview = ttk.Treeview(window, show='headings')
        treeview["columns"] = columns

        column_widths = [100, 80, 40, 60, 40, 40, 40, 40, 60, 60]
        for column, width in zip(treeview["columns"], column_widths):
            treeview.column(column, width=width)

        for column in treeview["columns"]:
            treeview.heading(column, text=column)

        for index, row in self.df[columns].iterrows():
            treeview.insert("", tk.END, values=tuple(row))

        treeview.pack(fill="both", expand=True)

    def ButtonGraph_command(self):
        count_category = self.df['IPS'].value_counts()
        sort_category = count_category.sort_values(ascending=False)

        plt.figure(figsize=(8, 5))

        plt.scatter(count_category.index, sort_category, marker='o', color='red')
        plt.title('Grafik IPS Mahasiswa')
        plt.xlabel('Nilai')
        plt.ylabel('Jumlah Mahasiswa')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
