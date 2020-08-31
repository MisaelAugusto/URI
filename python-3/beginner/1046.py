# -*- coding: utf-8 -*-

H1, H2 = map(int, input().split())

if (H1 == H2):
  result = 24
elif (H1 < H2):
  result = (H2 - H1)
else:
  result =  24 - H1 + H2

print("O JOGO DUROU %d HORA(S)" % (result))