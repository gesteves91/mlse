import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('JM1.csv', header=None, index_col =0)

data.plot(kind='bar')
plt.ylabel('LOC_TOTAL')
plt.xlabel('label')
plt.title('LOC TOTAL X DEFECTS')

plt.show()
