# Импортируем зависимости
import numpy as np
from matplotlib import pyplot as plt
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Flatten

# Подготавливаем данные для обучения
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train / 255
x_test = x_test / 255
y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

# Задаем модель НС (оптимизатор Adam)
model = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(46, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Производим обучение
model.fit(x_train, y_train_cat, batch_size=16, epochs=5, validation_split=0.2)

print('Метрики для тестовой выборки: ')
model.evaluate(x_test, y_test_cat)

print('Данные о модели: ')
print(model.summary())

# Задаем модель НС (оптимизатор RMSProp)
model = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(46, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='RMSProp',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Производим обучение
model.fit(x_train, y_train_cat, batch_size=16, epochs=5, validation_split=0.2)

print('Метрики для тестовой выборки: ')
model.evaluate(x_test, y_test_cat)

print('Данные о модели: ')
print(model.summary())

# Задаем модель НС (моменты Нестерова (SGD))
model = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(46, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Производим обучение
model.fit(x_train, y_train_cat, batch_size=16, epochs=5, validation_split=0.2)

print('Метрики для тестовой выборки: ')
model.evaluate(x_test, y_test_cat)

print('Данные о модели: ')
print(model.summary())