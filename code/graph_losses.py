import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# plt.show()

with open('losses') as losses:
	a = losses.readlines()
# a = [i[-7:-1] for i in a[::2]]
a = [float(i[-7:-1]) for i in a if '/' not in i and 'model' not in i]
print(a)

pd.DataFrame({
	'epoch': np.arange(len(a)),
	'loss': a
	}).plot.line(x='epoch', y='loss', color='r', figsize=(20, 10)).set(title='bzip2d')