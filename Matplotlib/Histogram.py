import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_excel('Matplotlib/data_motor.xlsx')

labels = dataframe['Kapasitas Mesin (cc)'].tolist()
values = dataframe['Jumlah Helm'].tolist()

plt.bar(labels, values, color='green')
plt.title('Diagram Batang')
plt.xlabel('Kapasitas Mesin (cc)')
plt.ylabel('Jumlah Helm')
plt.show()
