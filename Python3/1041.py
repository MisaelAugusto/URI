# -*- coding: utf-8 -*-

X, Y = map(float, input().split())

if (X == Y == 0):
  ANSWER = "Origem"
elif (X == 0):
  ANSWER = "Eixo Y"
elif (Y == 0):
  ANSWER = "Eixo X"
elif (X > 0 and Y > 0):
  ANSWER = "Q1"
elif (X > 0):
  ANSWER = "Q4"
elif (Y > 0):
  ANSWER = "Q2"
else:
  ANSWER = "Q3"

print(ANSWER)