# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
  X, Y = map(int, input().split())

  start = min(X, Y) + 2 if(min(X, Y) % 2 != 0) else min(X, Y) + 1 

  answer = sum(range(start, max(X, Y), 2))

  print(answer)