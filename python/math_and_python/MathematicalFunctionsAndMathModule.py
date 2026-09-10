"""
Вычисление числа сочетаний C(n, k).

Число сочетаний показывает, сколькими способами можно выбрать
k элементов из n, если порядок не важен.

Formula:
    C(n, k) = n! / (k! · (n - k)!)

    где n! — факториал числа n (произведение 1·2·3·…·n).

Example:
    n = 5, k = 2:
        C(5, 2) = 5! / (2! · 3!)
                = 120 / (2 · 6)
                = 120 / 12
                = 10


📐 Формула
----------
            n!             n!
    C(n,k) = ───────  =  ──────────
            k!(n-k)!      k!·(n-k)!

Где n! — факториал (произведение 1·2·3·…·n).

📊 Пример
---------
    Пусть n = 5, k = 2:

              5!          120         120
    C(5,2) = ──────── = ────────── = ───── = 10
             2!·3!      2 · 6         12

✅ Ответ: 10 способов.
"""
import math

# ввод данных (переменные n, k в программе не менять)
n, k = map(int, input().split())

# здесь продолжите программу
Cnk = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(Cnk)


n, k = map(int, input().split())


def factorial(x):
    result = 1
    for i in range(1, x + 1):   # i = 1, 2, 3, ..., x
        result *= i             # result = result * i
    return result


Cnk = factorial(n) // (factorial(k) * factorial(n - k))
print(Cnk)
