import pandas as pd
from sklearn.preprocessing import StandardScaler

train_data = pd.read_csv('train/train_data.csv')
test_data = pd.read_csv('test/test_data.csv')

scaler = StandardScaler()
train_data['temperature'] = scaler.fit_transform(train_data[['temperature']])
test_data['temperature'] = scaler.transform(test_data[['temperature']])

train_data.to_csv('train/train_data_scaled.csv', index=False)
test_data.to_csv('test/test_data_scaled.csv', index=False)