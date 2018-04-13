import pandas as pd
import numpy as np

df = pd.read_csv('JM1.csv')

data = df[["LOC_TOTAL", "BRANCH_COUNT", "label"]]

print(data[:10])
