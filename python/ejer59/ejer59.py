import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df: pd.DataFrame = pd.read_csv('iris.data')
df.columns = pd.Index(['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
unique_values: np.ndarray = np.unique(df['class'])

# Transformar los valores de class a valores numéricos usando LabelEncoder()
df['numeric_values'] = LabelEncoder().fit_transform(df['class'])

for c in unique_values:
    df[c] = (df['class'] == c).astype(int)  # convierto True o False en valores enteros 1 o 0

print(df)
