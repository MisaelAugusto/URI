# -*- coding: utf-8 -*-

operation = input()

total = 0
for i in range(144):
  N = float(input())

  line = (i // 12)
  column = (i % 12) + 1
  if (column <= 5 and column <= line <= (11 - column)):
    total += N
  
answer = total if (operation == 'S') else (total / 30)

print("%.1f" % answer)