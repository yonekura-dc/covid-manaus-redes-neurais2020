import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


x = np.arange(20)
y = np.array([i*i for i in x])
df = pd.DataFrame()
df['x'] = x
df['y'] = y
sns.lineplot(x='x', y='y',data=df)
plt.show()
