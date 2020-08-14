# -*- coding: utf-8 -*-

T = int(input())

for i in range(T):
  test = input().split()

  PA, PB = int(test[0]), int(test[1])
  G1, G2 = float(test[2]), float(test[3])

  years = 0
  while ((PA <= PB) and (years <= 100)):
    PA = int(PA * (1.0 + (G1 / 100)))
    PB = int(PB * (1.0 + (G2 / 100)))

    years += 1

  print(("%d anos." % years) if (years <= 100) else "Mais de 1 seculo.")