# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
  X = int(input())
  if (X == 0):
    print("NULL")
  else:
    answer = "EVEN" if (X % 2 == 0) else "ODD"
    answer += " "
    answer += "POSITIVE" if (X > 0) else "NEGATIVE"

    print(answer)