# -*- coding: utf-8 -*-

C = int(input())
operation = input()

total = 0
for i in range(144):
  N = float(input())

  if (i == C):
    total += N
    C += 12

answer = total if (operation == 'S') else (total / 12)

print("%.1f" % answer)