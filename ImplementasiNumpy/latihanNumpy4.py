import numpy as np

np_array = np.genfromtxt('ImplementasiNumpy/Latihan soal.csv', delimiter=';', skip_header=1, skip_footer=1)
coloumn_7 = np_array[:, 6]
sort = np.sort(coloumn_7)
print(sort)
