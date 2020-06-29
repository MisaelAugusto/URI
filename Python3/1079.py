# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
  N1, N2, N3 = map(float, input().split())

  average = (N1 * 0.2) + (N2 * 0.3) + (N3 * 0.5)

  print("%.1f" % average)