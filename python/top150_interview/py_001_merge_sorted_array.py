"""Анализ задачи:
    - Выполнить слияние двух массивов данных.
    - Отсортировать в неубывающем порядке.

Планирование:
    0) Создать класс.
    1) Передать в параметры два массива с данными.
    2) Передать в параметры два числа m, n которые указвают на длинну каждого массива
        2.1) m, n - игнорируют при измерении длины масива 0, и [].
            2.1.1) m, n - в таком случае будут равны 0.
    3) В пространстве имен класса объявить метод объекта
        3.1) В теле метода merge произвести объединение двух списков (массивов)
        3.2) Результат слияния присвоить первой переменной nums1
    4) Полученный результат надо отсортировать (по возрастанию)

Тестирование:
    1) Тест с заполненными массивами.
    2) Тест с пустым nums2.
    3) Тест с пустым nums1.
    4) Тест, где оба массива пусты.
"""
import unittest

class Solution:
    def merge_lst(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:m + n] = sorted(nums1[:m] + nums2[:n])


class TestSolution(unittest.TestCase):
    def setUp(self):
        """Создание объекта Solution перед каждым тестом."""
        self.solution = Solution()

    def test_merge_lst_example1(self):
        """Тест для первого набора входных данных."""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.solution.merge_lst(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_merge_lst_with_empty_nums2(self):
        """Тест, если nums2 пуст."""
        nums1 = [1, 2, 3]
        m = 3
        nums2 = []
        n = 0
        self.solution.merge_lst(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_merge_lst_with_empty_nums1(self):
        """Тест, если nums1 содержит только 0-элементы."""
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [1, 2, 3]
        n = 3
        self.solution.merge_lst(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_merge_lst_with_both_empty(self):
        """Тест, если оба массива пусты."""
        nums1 = []
        m = 0
        nums2 = []
        n = 0
        self.solution.merge_lst(nums1, m, nums2, n)
        self.assertEqual(nums1, [])

if __name__ == "__main__":
    unittest.main()