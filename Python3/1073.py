# -*- coding: utf-8 -*-

N = int(input())

for i in range(2, N + 1):
  if (i % 2 == 0):
    print("%d^%d = %d" % (i, 2, i ** 2))