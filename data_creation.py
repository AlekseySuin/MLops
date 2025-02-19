import os
import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split


# Функция для генерации одного набора данных
def generate_temperature_data(n_days):
    temperatures = []
    for day in range(n_days):
        # Нормальная температура
        normal_temp = random.uniform(-10, 20)
        # Аномальная температура
        anomaly_temp = random.choice([-50, 50])
        # Выбираем случайно между нормальной и аномальной температурой
        temperature = random.choice([normal_temp, anomaly_temp])
        temperatures.append(round(temperature, 1))

    df = pd.DataFrame({"day": list(range(n_days)), "temperature": temperatures})
    return df


# Настройки для генерации данных
num_train_sets = 3  # Количество тренировочных наборов
num_test_sets = 2  # Количество тестовых наборов

# Создаем каталоги train и test, если они еще не существуют
if not os.path.exists("train"):
    os.makedirs("train")
if not os.path.exists("test"):
    os.makedirs("test")

# Генерация тренировочных наборов данных
for i in range(num_train_sets):
    df = generate_temperature_data(365)  # 365 дней в году
    filename = f"train/temp_data_{i}.csv"
    df.to_csv(filename, index=False)
    print(f"Создан файл {filename}")

# Генерация тестовых наборов данных
for i in range(num_test_sets):
    df = generate_temperature_data(90)  # 90 дней для теста
    filename = f"test/temp_data_{i}.csv"
    df.to_csv(filename, index=False)
    print(f"Создан файл {filename}")

def save_data(X_test, X_train, y_test, y_train):
	...


#X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.10, random_state=42)