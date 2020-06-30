import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('../processed_data/processed_wikihow.csv')

X_train, X_test = train_test_split(data, test_size=0.1, random_state=42)

print(X_train, X_test.shape)