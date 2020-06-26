# -*- coding: utf-8 -*-

result = [0, 0, 0, 0]
resultText = ["par(es)", "impar(es)", "positivo(s)", "negativo(s)"]

for i in range(5):
  number = int(input())
  
  if (number % 2 == 0):
    result[0] += 1
  else:
    result[1] += 1
  
  if (number > 0):
    result[2] += 1
  elif (number < 0):
    result[3] += 1

for i in range(4):
  print("%d valor(es) %s" % (result[i], resultText[i]))
