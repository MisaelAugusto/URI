# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
  X, Y = map(int, input().split())

  start = X if (X % 2 != 0) else X + 1

  answer = sum(range(start, start + (2 * Y), 2))

  print(answer)