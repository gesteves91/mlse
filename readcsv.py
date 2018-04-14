import pandas as pd
import numpy as np

df = pd.read_csv('JM1.csv')

print(df.groupby('label')['LOC_TOTAL'].mean())
