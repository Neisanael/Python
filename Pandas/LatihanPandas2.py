import pandas as pd

nama_file = 'Pandas/data_motor.xlsx'
df = pd.read_excel(nama_file)

data = {
    'Merek': ['Yamaha'],
    'Jenis': ['MT-15'],
    'Plat Asal': ['AB'],
    'Kapasitas Mesin (cc)': [250],
    'Jumlah Helm': [2]
}
new_df = pd.DataFrame(data)

df = pd.concat([df, new_df], ignore_index=True)

df.to_excel(nama_file, index=False)
