test_list_1 = [1, 1, 2, 3]
test_list_2 = [1, 2, 0, 1, 2, -1, 0, 3]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Удаляет дубликаты и меняет исходный список на месте
        сортируя его по увеличению.

        Вход: Неотсортированный список целых чисел.

        Выход: Изменённый исходный,
               отсортированный список целых чисел и его длина.
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums), nums


solution = Solution()
print(solution.removeDuplicates(test_list_2))
print(test_list_2)