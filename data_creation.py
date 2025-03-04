import numpy as np
import pandas as pd
import os

os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

np.random.seed(42)
days = np.arange(1, 101)
temperature = 20 + 0.5 * days + np.random.normal(0, 5, 100)

temperature[50:55] += 20

train_data = pd.DataFrame({'day': days[:80], 'temperature': temperature[:80]})
test_data = pd.DataFrame({'day': days[80:], 'temperature': temperature[80:]})

train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)