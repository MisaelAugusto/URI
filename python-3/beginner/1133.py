# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())

start, end = min(X, Y), max(X, Y)

for i in range(start + 1, end):
  if ((i % 5) in [2, 3]):
    print(i)