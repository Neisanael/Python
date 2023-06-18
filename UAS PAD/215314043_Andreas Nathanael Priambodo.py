import tkinter as tk
import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Jengkol:
    def __init__(self, provinsi, jengkol):
        self.provinsi = provinsi
        self.jengkol = jengkol

class App:
    def __init__(self, root):
        self.table_frame = None
        self.pie_frame = None

        self.cnx = None
        self.cursor = None

        self.canvasHistogram = None
        #setting window size
        width=410
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Create Label Provinsi
        LabelProvinsi = tk.Label(root)
        LabelProvinsi["text"] = "Provinsi : "
        LabelProvinsi.place(x=5,y=50,width=70,height=25)

        self.provinsi_entry = tk.Entry(root)
        self.provinsi_entry.place(x=65, y=50, width=125, height=25)

        # Create Label Berat (Ton)
        LabelBerat = tk.Label(root)
        LabelBerat["text"] = "Berat (Ton) : "
        LabelBerat.place(x=200,y=50,width=70,height=25)

        self.jengkol_entry = tk.Entry(root)
        self.jengkol_entry.place(x=270, y=50, width=125, height=25)

        # Create Label Maksimal
        self.LabelMaks = tk.Label(root)
        self.LabelMaks["text"] = "Maksimal : "
        self.LabelMaks.place(x=50, y=90, width=100, height=25)

        # Create Label Minimal
        self.LabelMins = tk.Label(root)
        self.LabelMins["text"] = "Minimal : "
        self.LabelMins.place(x=50, y=120, width=100, height=25)

        # Create Label Rata - rata
        self.LabelAvg = tk.Label(root)
        self.LabelAvg["text"] = "Rata - rata : "
        self.LabelAvg.place(x=50, y=150, width=100, height=25)

        #Create Label Status
        self.LabelStatus = tk.Label(root)
        self.LabelStatus["text"] = ""
        self.LabelStatus["fg"] = "red"
        self.LabelStatus.place(x=5, y=180, width=100, height=25)

        ConnectButton=tk.Button(root)
        ConnectButton["text"] = "Connect"
        ConnectButton.place(x=10,y=10,width=70,height=25)
        ConnectButton["command"] = self.ConnectButton_command

        InsertButton=tk.Button(root)
        InsertButton["text"] = "Insert"
        InsertButton.place(x=90,y=10,width=70,height=25)
        InsertButton["command"] = self.InsertButton_command

        StatistikButton=tk.Button(root)
        StatistikButton["text"] = "Statistik"
        StatistikButton.place(x=170,y=10,width=70,height=25)
        StatistikButton["command"] = self.StatistikButton_command

        GrafikButton=tk.Button(root)
        GrafikButton["text"] = "Grafik"
        GrafikButton.place(x=250,y=10,width=70,height=25)
        GrafikButton["command"] = self.GrafikButton_command

        ExportButton=tk.Button(root)
        ExportButton["text"] = "Export"
        ExportButton.place(x=330,y=10,width=70,height=25)
        ExportButton["command"] = self.ExportButton_command

    def CreateTable(self, data):
        total_rows = len(data)
        total_columns = len(data[0])
        if self.table_frame is not None and self.table_frame.winfo_exists():
            self.table_frame.destroy()
        self.table_frame = tk.Toplevel(root)

        # Create a canvas
        canvas = Canvas(self.table_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Create a vertical scroll bar
        scrollbar = Scrollbar(self.table_frame, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Configure the canvas to use the scroll bar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # Create a frame inside the canvas
        frame = Frame(canvas)

        canvas.create_window((0, 0), window=frame)
        for i in range(total_rows):
            for j in range(total_columns):
                value = data[i][j]
                label = Label(frame, width=20, text=value)
                label.grid(row=i, column=j)

    def getData(self):
        self.cursor.execute("SELECT * FROM jengkol")
        rows = self.cursor.fetchall()
        jengkol_objects = []
        for row in rows:
            provinsi = row[0]
            jengkol = row[1]
            jengkol_obj = Jengkol(provinsi, jengkol)
            jengkol_objects.append(jengkol_obj)
        return jengkol_objects

    def ConnectButton_command(self):
        try:
            # Establish a connection
            self.cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="jengkol"
            )

            self.cursor = self.cnx.cursor()
            self.LabelStatus["text"] = ""

            #creating new Table
            data = self.getData()
            data_tuples = [(obj.provinsi, obj.jengkol) for obj in data]
            self.CreateTable(data_tuples)
            
        except mysql.connector.Error as error:
            print("Error connecting to the database:", error)

    def InsertButton_command(self):
        provinsi_value = self.provinsi_entry.get()
        jengkol_value = self.jengkol_entry.get()
        
        if self.cursor:
            if provinsi_value == "" or jengkol_value == "":
                self.LabelStatus["text"] = "No Data!"
            else:
                # Access the cursor object and perform the insert operation
                self.cursor.execute("INSERT INTO `jengkol`(`provinsi`, `ton`) VALUES (%s, %s)", (provinsi_value, jengkol_value))
                self.cnx.commit()
                #creating new Table
                data = self.getData()
                data_tuples = [(obj.provinsi, obj.jengkol) for obj in data]
                self.CreateTable(data_tuples)
            
        else:
            self.LabelStatus["text"] = "Connect First!"

    def StatistikButton_command(self):
        if self.cursor:
            # Access the cursor object and perform the insert operation
            data = self.getData()
            jengkol_values = [obj.jengkol for obj in data]
            if len(jengkol_values) > 0: 
            # Calculate the maximum, minimum, and average using NumPy
                max_value = np.max(jengkol_values)
                min_value = np.min(jengkol_values)
                avg_value = np.mean(jengkol_values)
            
            # Update the label texts with the calculated values
            self.LabelMaks["text"] = f"Maksimal: {max_value}"
            self.LabelMins["text"] = f"Minimal: {min_value}"
            self.LabelAvg["text"] = f"Rata - rata: {avg_value}"

        else:
            self.LabelStatus["text"] = "Connect First!"

    def GrafikButton_command(self):
        if self.cursor:
            data = self.getData()
            data_tuples = [(obj.provinsi, obj.jengkol) for obj in data]

            self.fig, ax = plt.subplots()
            labels = [entry[0] for entry in data_tuples]
            jengkol_values = [entry[1] for entry in data_tuples]

            x_pos = np.arange(len(labels))

            ax.bar(x_pos, jengkol_values, align='center')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(labels, rotation=90)
            ax.set_xlabel('Provinsi')
            ax.set_ylabel('Berat (Ton)')
            ax.set_title('Berat Jengkol per Provinsi')

            if self.pie_frame is not None and self.pie_frame.winfo_exists():
                self.pie_frame.destroy()
            

            self.pie_frame = tk.Toplevel(root)

            self.canvasHistogram = FigureCanvasTkAgg(self.fig, master=self.pie_frame)
            self.canvasHistogram.get_tk_widget().config(width=900, height=700)
            self.canvasHistogram.draw()
            self.canvasHistogram.get_tk_widget().pack()

            self.fig.tight_layout()

            self.CreateTable(data_tuples)


        else:
            self.LabelStatus["text"] = "Connect First!"

    def ExportButton_command(self):
        if self.cursor:
            # Sample data
            data = self.getData()
            data_tuples = [(obj.provinsi, obj.jengkol) for obj in data]
            column1 = [entry[0] for entry in data_tuples]
            column2 = [entry[1] for entry in data_tuples]

            # Create a dictionary with column names as keys and data lists as values
            data = {'Provinsi': column1, 'Jengkol (Ton)': column2}

            # Convert the dictionary to a pandas DataFrame
            df = pd.DataFrame(data)

            # Specify the file path for the Excel file
            file_path = 'data.xlsx'

            # Export the DataFrame to Excel
            df.to_excel(file_path, index=False)

        else:
            self.LabelStatus["text"] = "Connect First!"
    
    def on_window_close(self):
        if self.canvasHistogram is not None and self.canvasHistogram.get_tk_widget().winfo_exists():
            self.canvasHistogram.get_tk_widget().destroy()
            self.canvasHistogram.get_tk_widget().quit()
            plt.close(self.fig)
        if self.pie_frame is not None and self.pie_frame.winfo_exists():
            self.pie_frame.destroy()
            self.pie_frame.quit()
        if self.table_frame is not None and self.table_frame.winfo_exists():
            self.table_frame.destroy()
            self.table_frame.quit()
        root.destroy()
        root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.on_window_close)
    root.mainloop()
