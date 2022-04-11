# -*- coding: utf-8 -*-
"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия. Программа должна определить среднюю
прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter, deque, OrderedDict, namedtuple

print(__doc__)
k = int(input("Количество предприятий: "))
enterprises = OrderedDict()
QuarterProfit = namedtuple("QuarterProfit", "first second third fourth")

for i in range(1, k+1):
    name = input(f"{i} Наименование предприятия: ")
    fmt = f"{i} Прибыль предприятия за %s квартал: "
    enterprises[name] = QuarterProfit(
            float(input(fmt % "1ый")),
            float(input(fmt % "2ой")),
            float(input(fmt % "3ий")),
            float(input(fmt % "4ый"))
    )

average_profit = sum(deque(map(sum, deque(enterprises.values())))) / k
print(f"Средняя прибыль за год = {average_profit}")

more_less = Counter({name: (sum(profits) - average_profit) for name, profits in
                     enterprises.items()})
print(f"Предприятия с прибылью выше среднего: {deque((+more_less).keys())}")
print(f"Предприятия с прибылью выше среднего: {deque((-more_less).keys())}")
