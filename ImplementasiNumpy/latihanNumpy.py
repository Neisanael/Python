import numpy as np

np_array = np.genfromtxt('ImplementasiNumpy/Latihan soal.csv', delimiter=';', skip_header=1, dtype=str)

print(np_array)