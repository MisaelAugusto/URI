# -*- coding: utf-8 -*-

salary = float(input())

if (salary > 4500):
  taxes = (salary - 4500) * 0.28 + 350
elif (3000.01 <= salary <= 4500):
  taxes = (salary - 3000) * 0.18 + 80
elif (2000.01 <= salary <= 3000):
  taxes = (salary - 2000) * 0.08
else:
  taxes = 0

print("Isento" if (taxes == 0) else "R$ %.2f" % taxes)
