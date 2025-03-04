import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

train_data = pd.read_csv('train/train_data_scaled.csv')

X_train = train_data[['day']]
y_train = train_data['temperature']

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')