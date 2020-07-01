# -*- coding: utf-8 -*-

while (True):
  M, N = map(int, input().split())

  if (M <= 0 or N <= 0):
    break

  sequence = list(range(min(M, N), max(M, N) + 1))

  answer = " ".join(map(str, sequence)) + " Sum=%d"

  print(answer % sum(sequence))
