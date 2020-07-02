# -*- coding: utf-8 -*-

N = int(input())

start = 1
for i in range(N):
  print(" ".join(map(str, range(start, start + 3))) + " PUM")
  start += 4