import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Matplotlib/data_motor.xlsx')

helm_count = df.groupby('Merek')['Jumlah Helm'].sum()
labels = helm_count.index.tolist()
values = helm_count.values.tolist()

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Diagram Pie Jumlah Helm')
plt.show()
