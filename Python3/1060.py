# -*- coding: utf-8 -*-

positives = 0
for i in range(6):
  number = float(input())

  if (number > 0):
    positives += 1

print("%d valores positivos" % positives)