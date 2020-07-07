# -*- coding: utf-8 -*-

operation = input()

total = 0
for i in range(144):
  N = float(input())

  line = (i // 12) + 1
  inMiddle = (line * 12 - line) < i < 13 * (line - 1)
  if (line >= 8 and inMiddle):
    total += N

answer = total if (operation == 'S') else (total / 30)

print("%.1f" % answer)