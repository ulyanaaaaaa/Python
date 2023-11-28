import matplotlib.pyplot as plt
import numpy as np

a_start=3.5
a_end=25.5
a_delta=0.75
x=3.567

a_val=np.arange(a_start, a_end+a_delta, a_delta) #возвращает массив элементов
y_val=[]

for a in a_val:
    y = 1 / np.tan(x ** 3) + 2.24 * a * x
    y_val.append(y) #добавить фрейм данных y_val в конец фрейма данных y

for a, y in zip(a_val, y_val): #zip-сложение 2 объектов в 1
    print(f"a = {a:.2f}, y = {y:.2f}")

max_y=max(y_val)
min_y=min(y_val)
mean_y=np.mean(y_val) #вычисление среднего арифметического

print("Max value:",max_y)
print("Min value: ", min_y)
print("Average value:",mean_y)

sorted_y_values=sorted(y_val)

plt.figure(figsize=(10,6)) #создание фигуры
plt.plot(a_val, y_val, label="f(a)", marker='*') #ломанная линия
plt.axhline(mean_y, color='blue', linestyle='dotted', label="Среднее значение") #горизонтальная линия
plt.title("График функции f(a)")
plt.grid(True) #отрисовка координатной сетки на графике
plt.legend()
plt.show()
