# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
  X = int(input())

  total = 0
  for i in range(1, int((X / 2)) + 1):
    if (X % i == 0):
      total += i
  
  print(("%d eh perfeito" % X) if (total == X) else ("%d nao eh perfeito" % X))