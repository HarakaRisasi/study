
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
val = 3


class RemoveElSolution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Метод removeElement удаляет заданное значение из списка чисел и
        возвращает количество удалённых элементов.

        Параметры:
            nums — список чисел.
            val — значение, которое необходимо удалить из списка.

        Возвращаемое значение:
            Метод возвращает количество удалённых элементов из списка nums.
        """

        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        return len(nums)


remove_el = RemoveElSolution()
print(remove_el.removeElement(nums, val))