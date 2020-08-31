# -*- coding: utf-8 -*-

A, B, C = sorted(map(float, input().split()), reverse=True)

conditions = [A >= (B + C), A**2 == (B**2 + C**2), A**2 > (B**2 + C**2),
              A**2 < (B**2 + C**2), A == B == C,
              (A == B != C) or (A != B == C) or (A == C != B)]
messages = ["NAO FORMA TRIANGULO", "TRIANGULO RETANGULO", "TRIANGULO OBTUSANGULO",
            "TRIANGULO ACUTANGULO", "TRIANGULO EQUILATERO", "TRIANGULO ISOSCELES"]

for i in range(6):
  if (conditions[i]):
    print (messages[i])
    if (i == 0): break