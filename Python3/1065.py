# -*- coding: utf-8 -*-

evens = 0
for i in range(5):
  number = int(input())
  
  if (number % 2 == 0):
    evens += 1

print("%d valores pares" % evens)