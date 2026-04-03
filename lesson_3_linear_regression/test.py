import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split

# Замість load_boston імпортуємо fetch_openml
from sklearn.datasets import fetch_openml

# Завантажуємо датасет
boston = fetch_openml(data_id=531, as_frame=True, parser='auto')

# Оскільки ми використали as_frame=True, boston.data — це вже готовий DataFrame,
# тому нам не потрібно створювати його вручну через pd.DataFrame.
df = boston.data

# Цільова змінна
y = boston.target

# Можете перевірити, що все працює:
print(df.head())