"""
Map, filter и reduce — это три функции, которые используются для работы с
последовательностями в Python. Они имеют разные цели и способы использования.

Map применяет указанную функцию к каждому элементу последовательности и
возвращает новый список с результатами. Это полезно, когда нужно преобразовать
каждый элемент последовательности в соответствии с определённым правилом.

Filter фильтрует последовательность и возвращает только те элементы, которые
удовлетворяют заданному условию. Это полезно, когда нужно выбрать подмножество
элементов из последовательности на основе некоторого критерия.

Reduce сводит последовательность к одному значению, применяя указанную функцию
к элементам последовательности. Это полезно, когда нужно вычислить некоторое
значение на основе всех элементов последовательности.


Описание различий между этими функциями:
- map
Функция	Цель - Преобразование элементов последовательности.
Пример использования -  Возведение каждого элемента списка в квадрат

- filter
Функция	Цель - Выбор подмножества элементов из последовательности.
Пример использования -  Выбор только чётных чисел из списка.

- reduce
Функция	Цель - Вычисление значения на основе всех элементов последовательности.
Пример использования -  Нахождение суммы всех элементов списка.
"""
from functools import reduce


# Пример использования map
def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

print(list(squared_numbers))


# Пример использования filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))


# Пример использования reduce:
def add(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)

print(sum_of_numbers)



def solution(nums, value):
    count = nums.count(value)
    for i in range(count):
        nums.remove(value)
    return len(nums)
