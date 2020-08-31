# -*- coding: utf-8 -*-

A, B, C = map(float, input().split())

isTriangle = (A + B > C) and (A + C > B) and (B + C) > A

if (isTriangle):
  print ("Perimetro = %.1f" % (A + B + C))
else:
  print ("Area = %.1f" % ((A + B) * C / 2))