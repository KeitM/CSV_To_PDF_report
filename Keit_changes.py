import numpy as np
import pandas as pd
import polars as pl
import csv

from pandas import DataFrame  as df

from datetime import datetime

# for monitoring progress
from tqdm import tqdm

import seaborn as sns # plots for statistical analysis
import matplotlib.pyplot as plt # for data visualization

chunk_size = 10000

# # Чтение файла по частям
# chunks = pd.read_csv('btcusd_1-min_data.csv', chunksize=chunk_size)

# with pd.read_csv('btcusd_1-min_data.csv', chunksize=chunk_size) as reader:
#     for chunk in reader:
#         with open('btcusd_1-min_data.csv', 'r') as file:
#             reader = csv.reader(file)
#            # df = pd.DataFrame(reader)
#            # next(reader) 
#             for row in reader:
#                  for column in reader:
#                 #     chunk['timestamp'].head()
#                 #     df['date'] = pd.to_datetime(df['timestamp_ms'], unit='ms')  
#                 #  #   reader['timestamp'] = pd.Timestamp.to_datetime(train_full['timestamp'])
#                     print(row)
                    


# Чтение файла по частям


averages = []

with pd.read_csv('btcusd_1-min_data.csv', chunksize=chunk_size) as reader:
    for i, chunk in enumerate(reader):
        print(f"Обработка порции {i + 1}...")

       
        if 'Timestamp' in chunk.columns:
            chunk['date'] = pd.to_datetime(chunk['Timestamp'], unit='ms')
      
        else:
            print("Нет подходящего столбца с timestamp")
            continue
        
        
        if 'Open' in chunk.columns:
            avg_Open = chunk['Open'].mean()
            averages.append({'chunk': i+1, 'avg_Open': avg_Open})
        else:
            averages.append({'chunk': i+1, 'avg_Open': None})
        
        
        # Теперь можешь работать с chunk, например:
     #   print(chunk[['date']].head())  # Вывести первые строки текущей порции
        print(averages)