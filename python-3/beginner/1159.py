# -*- coding: utf-8 -*-

while (True):
  X = int(input())

  if (X == 0):
    break

  start = X if (X % 2 == 0) else X + 1

  answer = sum(range(start, start + 10, 2))

  print(answer)