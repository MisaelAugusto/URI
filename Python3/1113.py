# -*- coding: utf-8 -*-

while (True):
  X, Y = map(int, input().split())

  if (X == Y):
    break

  print("Crescente" if (X < Y) else "Decrescente")