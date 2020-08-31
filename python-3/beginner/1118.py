# -*- coding: utf-8 -*-

def scores_and_validation():
  n, media = 0, 0
  while (n < 2):
    note = float(input())

    if (note < 0 or note > 10):
      print("nota invalida")
    else:
      media += note
      n += 1

  print("media = %.2f" % (media / 2))

while (True):
  scores_and_validation()
  
  option = 0
  while(not(option in [1, 2])):
    option = int(input("novo calculo (1-sim 2-nao)\n"))
  
  if (option == 2):
    break
