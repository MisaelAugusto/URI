# -*- coding: utf-8 -*-

operation = input()

total = 0
for i in range(144):
  N = float(input())

  line = (i // 12) + 1
  if (i > (line * 12 - line)):
    total += N

answer = total if (operation == 'S') else (total / 66)

print("%.1f" % answer)