# Богданов Алексей Максимович, лабораторная 3, второй семестр

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

# Каталог с данными для обучения
train_dir = 'train'
# Каталог с данными для проверки
val_dir = 'val'
# Размеры изображения
img_width, img_height = 32, 32
# Размерность тензора на основе изображения для входных данных в нейронную сеть
# backend Tensorflow, channels_last
input_shape = (img_width, img_height, 3)
# Количество эпох
epochs = 5
# Размер мини-выборки
batch_size = 16

model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('relu'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
datagen = ImageDataGenerator(rescale=1. / 255)
train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')
val_generator = datagen.flow_from_directory(
    val_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')
history = model.fit_generator(
    train_generator,
    steps_per_epoch=100,
    epochs=epochs,
    validation_data=val_generator,
    validation_steps=50)
scores = model.evaluate_generator(val_generator, 50)
print("Аккуратность на тестовых данных: %.2f%%" % (scores[1] * 100))
# 100/100 [==============================] - 16s 153ms/step - loss: 1.5262 - accuracy: 0.9000
#                                                           - val_loss: 1.5425 - val_accuracy: 0.9000
print(model.summary())
# Model: "sequential"
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #
# =================================================================
# conv2d (Conv2D)              (None, 30, 30, 64)        1792
# _________________________________________________________________
# activation (Activation)      (None, 30, 30, 64)        0
# _________________________________________________________________
# max_pooling2d (MaxPooling2D) (None, 15, 15, 64)        0
# _________________________________________________________________
# flatten (Flatten)            (None, 14400)             0
# _________________________________________________________________
# dense (Dense)                (None, 64)                921664
# _________________________________________________________________
# activation_1 (Activation)    (None, 64)                0
# _________________________________________________________________
# dropout (Dropout)            (None, 64)                0
# _________________________________________________________________
# dense_1 (Dense)              (None, 1)                 65
# _________________________________________________________________
# activation_2 (Activation)    (None, 1)                 0
# =================================================================
# Total params: 923,521

# Весовой коэффициент - величина, определяющая степень влияния
# входного значения нейрона предшествующего слоя
# на связанный с ним нейрон текущего слоя.
#
# В данной модели каждый нейрон текущего слоя
# связан со всеми нейронами предыдущего слоя.
#
# Таким образом, для данной модели совокупность связей двух соседних слоёв
# есть декартово произведение нейронов этих слоёв.
#
# Следовательно, количество весовых коэффициентов для каждого слоя
# есть произведение числа нейронов этого слоя на число нейронов связанного с ним следующего слоя.
#
# 15 * 15 * 64 * 64 = 921 600
