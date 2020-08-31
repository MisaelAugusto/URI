# -*- coding: utf-8 -*-

operation = input()

total = 0
for i in range(144):
  N = float(input())

  line = (i // 12) + 1
  column = (i % 12)

  indexRight = (line * 12) - line
  indexRight += (2 * (line - 7) + 1) if (line > 6) else 0

  if (i > indexRight):
    total += N
  
answer = total if (operation == 'S') else (total / 30)

print("%.1f" % answer)