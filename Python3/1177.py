# -*- coding: utf-8 -*-

T = int(input())

temp = list(range(T))
for i in range(1000):
  print("N[%d] = %d" % (i, temp[i % T]))