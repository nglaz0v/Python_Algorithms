# -*- coding: utf-8 -*-
"""
Определить, является ли год, который ввёл пользователь, високосным или не
високосным.
"""

year = int(input("year: "))
if (year < 1582):
    print(f"{year} - это год до введения григорианского календаря")
else:
    century = year // 100
    if ((year % 100) == 0):
        if ((century % 4) == 0):
            print(f"Год {year} - високосный")
        else:
            print(f"Год {year} - невисокосный")
    else:
        if ((year % 4) == 0):
            print(f"Год {year} - високосный")
        else:
            print(f"Год {year} - невисокосный")
