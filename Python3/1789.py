# -*- coding: utf-8 -*-

while (True):
  try:
    L = int(input())
    speed = max(map(int, input().split()))

    answer = 3 if (speed >= 20) else (2 if (speed >= 10) else 1)

    print(answer)

  except EOFError:
    break