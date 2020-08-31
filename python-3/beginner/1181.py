# -*- coding: utf-8 -*-

L = int(input())
operation = input()

start = 12 * L
end = start + 11

total = 0
for i in range(144):
  N = float(input())

  if (start <= i <= end):
    total += N

answer = total if (operation == 'S') else (total / 12)

print("%.1f" % answer)