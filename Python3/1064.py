# -*- coding: utf-8 -*-

positives, total = 0, 0
for i in range(6):
  number = float(input())

  if (number > 0):
    positives += 1
    total += number

print("%d valores positivos" % positives)
print("%.1f" % (total / positives))