import numpy as np

# Создание массива чисел от 0 до 9
array = np.arange(25)

# Возведение в квадрат
squared_array = np.square(array)

# Среднее значение массива
mean_value = np.mean(array)

# Стандартное отклонение массива
std_deviation = np.std(array)

print(f"Исходный массив: {array}")
print(f"Возведение в квадрат: {squared_array}")
print(f"Среднее значение: {mean_value}")
print(f"Стандартное отклонение: {std_deviation}")