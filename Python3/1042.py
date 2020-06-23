# -*- coding: utf-8 -*-

A, B, C = map(int, input().split())

sortedNumbers = sorted([A, B, C])

for number in sortedNumbers:
  print(number)

print("")

print(A)
print(B)
print(C)