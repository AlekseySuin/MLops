import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

model = joblib.load('model.pkl')

test_data = pd.read_csv('test/test_data_scaled.csv')

X_test = test_data[['day']]
y_test = test_data['temperature']

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')