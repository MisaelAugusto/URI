# -*- coding: utf-8 -*-

while (True):
  X, Y = map(int, input().split())

  if (X == 0 or Y == 0):
    break

  if (X > 0 and Y > 0):
    answer = "primeiro"
  elif (X > 0):
    answer = "quarto"
  elif (Y > 0):
    answer = "segundo"
  else:
    answer = "terceiro"

  print(answer)