import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Matplotlib/data_motor.xlsx')

x = df['Kapasitas Mesin (cc)']
y = df['Jumlah Helm']

plt.scatter(x, y, color='blue')
plt.title('Diagram Scatter')
plt.xlabel('Kapasitas Mesin (cc)')
plt.ylabel('Jumlah Helm')
plt.show()
