# -*- coding: utf-8 -*-

N = int(input())

fib = [0]
for i in range(1, N):
  if (i <= 2):
    fib.append(1)
  else:
    fib.append(fib[-1] + fib[-2])

answer = " ".join(map(str, fib))

print(answer)