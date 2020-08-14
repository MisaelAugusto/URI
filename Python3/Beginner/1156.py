# -*- coding: utf-8 -*-

S, N, D = 0, 1, 1
while (N <= 39):
  S += (N / D)
  N += 2
  D *= 2


print("%.2f" % S)