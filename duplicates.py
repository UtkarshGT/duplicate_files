import pandas as pd
import os

file_names = os.listdir()

file_sizes = []

for file_name in file_names:
    file_sizes.append(os.path.getsize(file_name))

df = pd.DataFrame({'file_name': file_names, 'file_size': file_sizes})

duplicates = df.duplicated(subset='file_size', keep='last')

print(df[duplicates])
