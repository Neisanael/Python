import numpy as np

dtypes = [('col1', int), ('col2', 'U50'), ('col3', 'U50'), ('col4', int), ('col5', int), ('col6', int), ('col7', int)]

np_array = np.genfromtxt('ImplementasiNumpy/Latihan soal.csv', delimiter=';', skip_header=1, skip_footer=1, dtype=dtypes)

new_data = np.array([(115, 'John Doe', 'University XYZ', 18, 5, 2, 95)], dtype=dtypes)

updated_data = np.concatenate((np_array, new_data))

np.savetxt('ImplementasiNumpy/updated_data.csv', updated_data, delimiter=';', fmt='%s')
