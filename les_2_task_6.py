# -*- coding: utf-8 -*-
"""
В программе генерируется случайное целое число от 0 до 100. Пользователь должен
его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно
сообщаться, больше или меньше введённое пользователем число, чем то, что
загадано. Если за 10 попыток число не отгадано, вывести ответ.
"""

import random

print(__doc__)
n = random.randint(0, 100)
print("Отгадайте число от 0 до 100 за 10 попыток")
for i in range(10):
    x = int(input(f"[{i}] x: "))
    if (x < n):
        print("x < n")
    elif (x > n):
        print("x > n")
    else:
        print("x = n")
        break
else:
    print(f"Число не отгадано: {n}")
