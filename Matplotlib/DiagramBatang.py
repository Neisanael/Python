import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Matplotlib/data_motor.xlsx')

helm_count = df.groupby('Merek')['Jumlah Helm'].sum()
labels = helm_count.index.tolist()
values = helm_count.values.tolist()

plt.bar(labels, values, color='green')
plt.title('Diagram Batang Jumlah Helm')
plt.xlabel('Merek')
plt.ylabel('Jumlah Helm')
plt.show()
