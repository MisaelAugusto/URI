# -*- coding: utf-8 -*-

answer, position = 0, 0
for i in range(100):
  N = int(input())

  if (N > answer):
    answer = N
    position = i + 1

print(answer)
print(position)