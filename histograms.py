import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('JM1.csv')
data = data.head(1000)
data = data[["LOC_TOTAL", "label"]]

data.plot(kind='bar')
plt.ylabel('LOC_TOTAL')
plt.xlabel('label')
plt.title('LOC TOTAL X DEFECTS')

plt.show()
