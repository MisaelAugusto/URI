# -*- coding: utf-8 -*-

total, n = 0, 0
while(True):
  age = int(input())

  if (age < 0):
    break

  total += age
  n += 1

average = total / n

print("%.2f" % average)