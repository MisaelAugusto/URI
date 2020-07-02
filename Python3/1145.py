# -*- coding: utf-8 -*-

X, Y = map(int, input().split())

start = 1
while (start < Y):
  print(" ".join(map(str, range(start, start + X))))
  start += X