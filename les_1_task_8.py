# Вводятся три разных числа. Найти, какое из них является средним (больше
# одного, но меньше другого).

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
x = None
# Решение №1: перебор всех возможных (3! = 6) вариантов
if (a <= b) and (b <= c):
    x = b
elif (c <= b) and (b <= a):
    x = b
elif (a <= c) and (c <= b):
    x = c
elif (b <= c) and (c <= a):
    x = c
elif (b <= a) and (a <= c):
    x = a
else:
    x = a
print(x)

# Решение №2
lo = min(min(a, b), c)
hi = max(max(a, b), c)
x = (a + b + c) - lo - hi
print(x)
