# -*- coding: utf-8 -*-

n, media = 0, 0
while (n < 2):
  note = float(input())

  if (note < 0 or note > 10):
    print("nota invalida")
  else:
    media += note
    n += 1

print("media = %.2f" % (media / 2))