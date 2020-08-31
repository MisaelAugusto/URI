# -*- coding: utf-8 -*-

X = int(input())

while(True):
  Z = int(input())

  if (Z > X):
    break

total, answer = 0, 0
while(total < Z):
  total += X
  answer += 1

  X += 1

print(answer)