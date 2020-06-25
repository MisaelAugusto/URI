# -*- coding: utf-8 -*-

H1, M1, H2, M2 = map(int, input().split())

start, end = H1 * 60 + M1, H2 * 60 + M2

if (start == end):
  result = [24, 0]
elif (start < end):
  result = [(end - start) // 60, (end - start) % 60]
else:
  result = [(1440 - start + end) // 60, (1440 - start + end) % 60]

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (result[0], result[1]))