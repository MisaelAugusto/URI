# -*- coding: utf-8 -*-

for i in range(10):
  X = int(input())

  answer = 1 if (X <= 0) else X 

  print("X[%d] = %d" % (i, answer))