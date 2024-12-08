"""
Анализ задачи:
1. Реализовать класс `Point` для представления точки на плоскости.
2. Объект класса должен принимать:
   - Два обязательных аргумента `x` и `y` для задания координат.
   - Третий необязательный аргумент `color`, который по умолчанию равен `'black'`.
3. Создать 1000 объектов класса `Point` с координатами, увеличивающимися на 2: `(1, 1)`, `(3, 3)`, `(5, 5)` и так далее.
4. Добавить все созданные объекты в список `points`.
5. У второго объекта в списке `points` задать цвет `'yellow'`.

---

Планирование:
1. Объявить класс `Point`.
   - Создать метод `__init__`, который принимает `x`, `y` и необязательный параметр `color` (по умолчанию `'black'`).
   - Инициализировать локальные свойства объекта: `self.x`, `self.y` и `self.color`.
2. Создать пустой список `points` для хранения всех объектов.
3. Использовать цикл для создания 1000 объектов `Point`:
   - Для каждой итерации вычислить значения координат `x` и `y` как `1 + i * 2`.
   - Установить цвет `'yellow'` для второго объекта (индекс 1), для остальных — `'black'`.
   - Добавить созданный объект в список `points`.

---

Тестирование:
1. Проверить, что объекты создаются с правильными координатами `x` и `y`.
2. Проверить, что цвет по умолчанию равен `'black'`.
3. Убедиться, что второй объект имеет цвет `'yellow'`.
4. Проверить длину списка `points` — должно быть ровно 1000 элементов.
5. Проверить, что координаты объектов соответствуют правилам генерации.
"""

import unittest

class Point:
    def __init__(self, x: int, y: int, color='black') -> None:
        self.x = x
        self.y = y
        self.color = color

points = []

for i in range(1000):
    x = y = 1 + i * 2
    color = 'yellow' if i == 1 else 'black'
    points.append(Point(x, y, color))


class TestPoint(unittest.TestCase):
    def test_point_coordinates(self):
        """Проверить, что объекты создаются с правильными координатами x и y."""
        p1 = Point(10, 20)
        self.assertEqual((p1.x, p1.y), (10, 20))

    def test_default_color(self):
        """Проверить, что цвет по умолчанию равен 'black'."""
        p1 = Point(10, 20)
        self.assertEqual(p1.color, 'black')

    def test_second_point_color(self):
        """Убедиться, что второй объект имеет цвет 'yellow'."""
        self.assertEqual(points[1].color, 'yellow')

    def test_points_list_length(self):
        """Проверить длину списка points — должно быть ровно 1000 элементов."""
        self.assertEqual(len(points), 1000)

    def test_points_generation(self):
        """Проверить, что координаты объектов соответствуют правилам генерации."""
        for i, point in enumerate(points):
            expected_x = expected_y = 1 + i * 2
            self.assertEqual((point.x, point.y), (expected_x, expected_y))


if __name__ == "__main__":
    unittest.main()