# Вводятся три разных числа. Найти, какое из них является средним (больше
# одного, но меньше другого).

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
x = 0
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
