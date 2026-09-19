digit = int(input())

# Превращаем число в строку и получаем список его цифр
sum_digit = sum(int(d) for d in str(digit))
