# -*- coding: utf-8 -*-

salary = float(input())

dic = { 0 <= salary <= 400.00 : 0.15,
        400.01 <= salary <= 800.00 : 0.12,
        800.01 <= salary <= 1200.00 : 0.1,
        1200.01 <= salary <= 2000.00 : 0.07,
        salary > 2000.00 : 0.04 }

earned = salary * dic[True]

print("Novo salario: %.2f" % (salary + earned))
print("Reajuste ganho: %.2f" % earned)
print("Em percentual: %d %%" % (dic[True] * 100))