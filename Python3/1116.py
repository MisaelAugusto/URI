# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
  X, Y = map(int, input().split())

  if (Y == 0):
    print("divisao impossivel")
    continue

  print("%.1f" % (X / Y))