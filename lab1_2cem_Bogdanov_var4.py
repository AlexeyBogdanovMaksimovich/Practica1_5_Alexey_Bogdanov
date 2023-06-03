# Импортируем зависимости
import numpy
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error

# Функция генерации наборов входных и выходных данных в заданном диапазоне
def generate(start, stop, step):
    a_ = numpy.arange(start, stop, step)
    b_ = numpy.arange(start, stop, step)
    data = numpy.asarray([[a0, b0] for a0 in a_ for b0 in b_])
    target = numpy.asarray([[a0 + 0.5, b0 + 2] for a0 in a_ for b0 in b_])
    return data, target

# Генерируем тренировочные и тестовые наборы данных
train_data, train_targets = generate(1, 100, 1)
test_data, test_targets = generate(101, 200, 4)

# Описываем модель НС с двумя входными нейронами (произвольные действительные числа)
# и двумя выходными
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(2,)),
    keras.layers.Dense(20, activation=tf.nn.relu),
    keras.layers.Dense(20, activation=tf.nn.relu),
    keras.layers.Dense(2)
])

# Создаем модель НС с использованием оптимизации по Adam и метрикой mean absolute percentage error(MAPE)
model.compile(optimizer='adam',
              loss='mape',
              metrics=['mape'])

# Производим обучение НС (кол-во epochs=5)
model.fit(train_data, train_targets, epochs=5, batch_size=1)

# Тестируем обученную НС
_, test_mape = model.evaluate(test_data, test_targets)
print('Test mean absolute percentage error:', test_mape)

a, b = float(input("Enter a: ")), float(input("Enter b: "))
predict = model.predict(np.array([[a, b]]))[0]
true = [a + 0.5, b + 2]
print(f"Model prediction: {predict}; "
      f"true value: {true}, "
      f"mape: {mean_absolute_percentage_error([true], [predict])}")

