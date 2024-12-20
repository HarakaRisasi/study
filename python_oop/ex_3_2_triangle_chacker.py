"""Анализ задачи
1. Определение цели:
    - Цель: Объявить класс TriangleChecker, который проверяет треугольник на истину
    - Функции:
        - если хотя бы одна сторона не число (не float или int)
            или хотя бы одно число меньше или равно нулю;
        - указанные числа a, b, c не могут являться длинами сторон треугольника;
        - стороны a, b, c образуют треугольник.

2. Ключевые детали реализации:
    - Входные данные:
        - Прочитайте из входного потока строку,
            содержащую три числа, разделенных пробелами.
    - Выходные данные:
        - Возвращает следующие коды (1, 2 или 3).

3. Требования к задаче:
    - Проверку параметров a, b, c проводить именно в таком порядке (1, 2, 3).

Планирование
1. Шаги выполнения задачи:
    - Объявить класс TriangleChecker.
    - Объявить метод is_triangle().
    - Сделать проверку входных данных по условиям:
        1 - если хотя бы одна сторона не число (не float или int)
            или хотя бы одно число меньше или равно нулю;
        2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
        3 - стороны a, b, c образуют треугольник.
    - Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами.
        Команда:
            a, b, c = map(int, input().split())
    - Создать объект tr класса TriangleChecker.
    - Передайте ему прочитанные значения a, b, c.
    - Вызвать метод is_triangle() из объекта tr
    - Вывести результат на экран (-> :int)

2. Ключевые элементы:
    - Класс (TriangleChecker)
    - Функция (is_triangle)
    - Объект (tr)"""


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        # Проверка на тип и значения сторон (исключаем булевые значения)
        if not all(isinstance(side, (int, float)) and not isinstance(side, bool) and side > 0 for side in
                   (self.a, self.b, self.c)):
            return 1

        # Проверка выполнения неравенства треугольника
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            return 2

        # Успешное прохождение всех проверок
        return 3


# Чтение входных данных
try:
    a, b, c = map(int, input("Введите три стороны треугольника через пробел: ").split())

    # Создание объекта и вызов метода
    tr = TriangleChecker(a, b, c)
    result = tr.is_triangle()

    # Вывод результата
    print(result)
except ValueError:
    print(1)