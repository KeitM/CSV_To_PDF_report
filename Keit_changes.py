import numpy as np
import pandas as pd
import polars as pl
import csv


from datetime import datetime

# for monitoring progress
from tqdm import tqdm

import seaborn as sns # plots for statistical analysis
import matplotlib.pyplot as plt # for data visualization

chunk_size = 10000

# Чтение файла по частям
chunks = pd.read_csv('btcusd_1-min_data.csv', chunksize=chunk_size)

with pd.read_csv('btcusd_1-min_data.csv', chunksize=chunk_size) as reader:
    for chunk in reader:
        with open('btcusd_1-min_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)