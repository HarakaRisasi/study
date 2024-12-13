class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(1, 200)
print(Vector.validate(5))

res = Vector.get_coord(v)
print(res)

print(Vector.norm2(5, 6))


class Stepik:
    def get_certificate(self):
        return False

st = Stepik()

st.get_certificate()
Stepik.get_certificate(st)

