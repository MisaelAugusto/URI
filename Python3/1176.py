# -*- coding: utf-8 -*-

T = int(input())

fib = [0, 1]
for i in range(T):
  N = int(input())

  while (len(fib) < N + 1):
    fib.append(fib[-1] + fib[-2])

  print("Fib(%d) = %d" % (N, fib[N]))