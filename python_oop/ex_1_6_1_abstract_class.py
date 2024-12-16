"""Объявите класс AbstractClass, объекты которого нельзя было бы создавать.

При выполнении команды: obj = AbstractClass()
Переменная obj должна ссылаться на строку с содержимым: "Ошибка: нельзя создавать объекты абстрактного класса"

P.S. В программе объявить только класс, выводить на экран ничего не нужно."""

class Point:
    def __new__(cls, *args, **kwargs): # cls - ссылается на сам класс.
        print("Call __new__ for " + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0): # self - ссылается на экземпляр класса.
        print("Call __init__ for " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 3) # Экземпляр класса не был создан.
print(pt)



class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"

obj = AbstractClass()