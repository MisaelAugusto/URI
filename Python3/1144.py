# -*- coding: utf-8 -*-

N = int(input())

for i in range(1, N + 1):
  print(" ".join(map(str, [i, i ** 2, i ** 3])))
  print(" ".join(map(str, [i, (i ** 2) + 1, (i ** 3) + 1])))